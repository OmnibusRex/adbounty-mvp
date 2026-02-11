"""
Unit tests for AdBounty API
"""

import pytest
from fastapi.testclient import TestClient
from main import app, users_db, channels_db, bounties_db

client = TestClient(app)


class TestHealth:
    """Health check tests"""
    
    def test_health_check(self):
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"


class TestAuthentication:
    """Authentication tests"""
    
    def test_telegram_auth_new_user(self):
        response = client.post(
            "/auth/telegram",
            params={"telegram_id": 123456789, "username": "testuser"}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert data["user"]["telegram_id"] == 123456789
        assert data["user"]["username"] == "testuser"
    
    def test_telegram_auth_existing_user(self):
        # First auth
        client.post(
            "/auth/telegram",
            params={"telegram_id": 987654321, "username": "existinguser"}
        )
        
        # Second auth (should return existing user)
        response = client.post(
            "/auth/telegram",
            params={"telegram_id": 987654321, "username": "existinguser"}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["message"] == "User already exists"


class TestChannels:
    """Channel verification tests"""
    
    def test_verify_channel(self):
        response = client.post(
            "/channels/verify",
            params={
                "channel_id": -1001234567890,
                "channel_name": "Tech News",
                "owner_id": 123456789,
                "subscribers": 50000,
                "niche": "technology"
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert data["channel"]["verified"] is True
    
    def test_get_verified_channels(self):
        # Verify a channel first
        client.post(
            "/channels/verify",
            params={
                "channel_id": -1001234567891,
                "channel_name": "Finance Hub",
                "owner_id": 123456789,
                "subscribers": 30000,
                "niche": "finance"
            }
        )
        
        # Get verified channels
        response = client.get("/channels/verified")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert data["count"] > 0


class TestBounties:
    """Bounty creation and management tests"""
    
    def test_create_bounty(self):
        response = client.post(
            "/bounties/create",
            json={
                "advertiser_id": 123456789,
                "ton_amount": 10.5,
                "ad_text": "Check out our new product!",
                "ad_link": "https://example.com",
                "target_channels": [-1001234567890],
                "deadline_days": 7
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert data["bounty"]["ton_amount"] == 10.5
        assert data["bounty"]["status"] == "pending"
    
    def test_get_bounty(self):
        # Create a bounty first
        create_response = client.post(
            "/bounties/create",
            json={
                "advertiser_id": 123456789,
                "ton_amount": 5.0,
                "ad_text": "Test ad",
                "ad_link": "https://test.com",
                "target_channels": [-1001234567890],
                "deadline_days": 7
            }
        )
        bounty_id = create_response.json()["bounty"]["bounty_id"]
        
        # Get bounty
        response = client.get(f"/bounties/{bounty_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert data["bounty"]["bounty_id"] == bounty_id
    
    def test_get_nonexistent_bounty(self):
        response = client.get("/bounties/nonexistent_bounty")
        assert response.status_code == 404


class TestBids:
    """Bid placement tests"""
    
    def test_place_bid(self):
        # Create a bounty first
        bounty_response = client.post(
            "/bounties/create",
            json={
                "advertiser_id": 123456789,
                "ton_amount": 10.0,
                "ad_text": "Test ad",
                "ad_link": "https://test.com",
                "target_channels": [-1001234567890],
                "deadline_days": 7
            }
        )
        bounty_id = bounty_response.json()["bounty"]["bounty_id"]
        
        # Place bid
        response = client.post(
            f"/bounties/{bounty_id}/bid",
            json={
                "bounty_id": bounty_id,
                "channel_owner_id": 987654321,
                "channel_id": -1001234567890
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert data["bid"]["status"] == "pending"
    
    def test_place_bid_on_nonexistent_bounty(self):
        response = client.post(
            "/bounties/nonexistent/bid",
            json={
                "bounty_id": "nonexistent",
                "channel_owner_id": 987654321,
                "channel_id": -1001234567890
            }
        )
        assert response.status_code == 404


class TestConfirmViews:
    """View confirmation and payout tests"""
    
    def test_confirm_views(self):
        # Create bounty
        bounty_response = client.post(
            "/bounties/create",
            json={
                "advertiser_id": 123456789,
                "ton_amount": 10.0,
                "ad_text": "Test ad",
                "ad_link": "https://test.com",
                "target_channels": [-1001234567890],
                "deadline_days": 7
            }
        )
        bounty_id = bounty_response.json()["bounty"]["bounty_id"]
        
        # Confirm views
        response = client.post(
            f"/bounties/{bounty_id}/confirm-views",
            json={
                "bounty_id": bounty_id,
                "channel_owner_id": 987654321
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert data["bounty"]["status"] == "confirmed"
        assert "transaction" in data


class TestTransactions:
    """Transaction history tests"""
    
    def test_get_transactions(self):
        response = client.get("/transactions/123456789")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert "transactions" in data


class TestBotEndpoints:
    """Bot integration endpoints"""
    
    def test_post_ad(self):
        # Create bounty first
        bounty_response = client.post(
            "/bounties/create",
            json={
                "advertiser_id": 123456789,
                "ton_amount": 10.0,
                "ad_text": "Test ad",
                "ad_link": "https://test.com",
                "target_channels": [-1001234567890],
                "deadline_days": 7
            }
        )
        bounty_id = bounty_response.json()["bounty"]["bounty_id"]
        
        # Post ad
        response = client.post(
            "/bot/post-ad",
            params={
                "bounty_id": bounty_id,
                "channel_id": -1001234567890
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
