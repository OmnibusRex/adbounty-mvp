"""
AdBounty Backend - FastAPI Application
Handles bounty creation, channel verification, escrow management, and bot integration
"""

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import logging

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="AdBounty API",
    description="Telegram Mini App for Ad Marketplace with TON Escrow",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================================
# Data Models
# ============================================================================

class User(BaseModel):
    telegram_id: int
    username: str
    wallet_address: Optional[str] = None
    created_at: datetime = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "telegram_id": 123456789,
                "username": "john_doe",
                "wallet_address": "EQDk2ImpM...",
                "created_at": "2024-02-11T00:00:00"
            }
        }

class Channel(BaseModel):
    channel_id: int
    channel_name: str
    subscribers: int
    niche: str
    verified: bool
    owner_id: int
    created_at: datetime = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "channel_id": -1001234567890,
                "channel_name": "Tech News",
                "subscribers": 50000,
                "niche": "technology",
                "verified": True,
                "owner_id": 123456789
            }
        }

class CreateBountyRequest(BaseModel):
    advertiser_id: int
    ton_amount: float
    ad_text: str
    ad_link: str
    target_channels: List[int]
    deadline_days: int = 7
    
    class Config:
        json_schema_extra = {
            "example": {
                "advertiser_id": 123456789,
                "ton_amount": 10.5,
                "ad_text": "Check out our new product!",
                "ad_link": "https://example.com",
                "target_channels": [-1001234567890, -1001234567891],
                "deadline_days": 7
            }
        }

class Bounty(BaseModel):
    bounty_id: str
    advertiser_id: int
    ton_amount: float
    ad_text: str
    ad_link: str
    target_channels: List[int]
    status: str  # pending, posted, confirmed, completed, cancelled
    escrow_address: Optional[str] = None
    created_at: datetime = None
    deadline: datetime = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "bounty_id": "bounty_123",
                "advertiser_id": 123456789,
                "ton_amount": 10.5,
                "ad_text": "Check out our new product!",
                "ad_link": "https://example.com",
                "target_channels": [-1001234567890],
                "status": "pending",
                "escrow_address": "EQDk2ImpM...",
                "created_at": "2024-02-11T00:00:00",
                "deadline": "2024-02-18T00:00:00"
            }
        }

class BidRequest(BaseModel):
    bounty_id: str
    channel_owner_id: int
    channel_id: int
    
    class Config:
        json_schema_extra = {
            "example": {
                "bounty_id": "bounty_123",
                "channel_owner_id": 987654321,
                "channel_id": -1001234567890
            }
        }

class ConfirmViewsRequest(BaseModel):
    bounty_id: str
    channel_owner_id: int
    proof_url: Optional[str] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "bounty_id": "bounty_123",
                "channel_owner_id": 987654321,
                "proof_url": "https://example.com/proof.jpg"
            }
        }

class Transaction(BaseModel):
    tx_id: str
    from_user: int
    to_user: int
    amount: float
    tx_type: str  # deposit, payout, refund
    status: str  # pending, success, failed
    bounty_id: Optional[str] = None
    tx_hash: Optional[str] = None
    created_at: datetime = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "tx_id": "tx_123",
                "from_user": 123456789,
                "to_user": 987654321,
                "amount": 10.5,
                "tx_type": "payout",
                "status": "success",
                "bounty_id": "bounty_123",
                "tx_hash": "0x123abc...",
                "created_at": "2024-02-11T00:00:00"
            }
        }

# ============================================================================
# In-memory storage (replace with database in production)
# ============================================================================

users_db = {}
channels_db = {}
bounties_db = {}
bids_db = {}
transactions_db = {}

# ============================================================================
# Endpoints
# ============================================================================

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "AdBounty API"
    }

@app.post("/auth/telegram")
async def telegram_auth(telegram_id: int, username: str):
    """Authenticate user via Telegram"""
    try:
        if telegram_id in users_db:
            return {
                "status": "success",
                "message": "User already exists",
                "user": users_db[telegram_id]
            }
        
        user = User(
            telegram_id=telegram_id,
            username=username,
            created_at=datetime.utcnow()
        )
        users_db[telegram_id] = user.model_dump()
        
        logger.info(f"User authenticated: {telegram_id}")
        return {
            "status": "success",
            "message": "User authenticated",
            "user": user.model_dump()
        }
    except Exception as e:
        logger.error(f"Auth error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/channels/verified")
async def get_verified_channels():
    """Get list of verified channels"""
    try:
        verified = [ch for ch in channels_db.values() if ch.get("verified")]
        return {
            "status": "success",
            "count": len(verified),
            "channels": verified
        }
    except Exception as e:
        logger.error(f"Error fetching channels: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/channels/verify")
async def verify_channel(channel_id: int, channel_name: str, owner_id: int, subscribers: int, niche: str):
    """Verify a Telegram channel"""
    try:
        channel = Channel(
            channel_id=channel_id,
            channel_name=channel_name,
            subscribers=subscribers,
            niche=niche,
            verified=True,
            owner_id=owner_id,
            created_at=datetime.utcnow()
        )
        channels_db[channel_id] = channel.model_dump()
        
        logger.info(f"Channel verified: {channel_id}")
        return {
            "status": "success",
            "message": "Channel verified",
            "channel": channel.model_dump()
        }
    except Exception as e:
        logger.error(f"Channel verification error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/bounties/create")
async def create_bounty(request: CreateBountyRequest):
    """Create a new bounty"""
    try:
        bounty_id = f"bounty_{len(bounties_db) + 1}"
        deadline = datetime.utcnow() + timedelta(days=request.deadline_days)
        
        bounty = Bounty(
            bounty_id=bounty_id,
            advertiser_id=request.advertiser_id,
            ton_amount=request.ton_amount,
            ad_text=request.ad_text,
            ad_link=request.ad_link,
            target_channels=request.target_channels,
            status="pending",
            created_at=datetime.utcnow(),
            deadline=deadline
        )
        bounties_db[bounty_id] = bounty.model_dump()
        
        logger.info(f"Bounty created: {bounty_id}")
        return {
            "status": "success",
            "message": "Bounty created",
            "bounty": bounty.model_dump()
        }
    except Exception as e:
        logger.error(f"Bounty creation error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/bounties/{bounty_id}")
async def get_bounty(bounty_id: str):
    """Get bounty details"""
    try:
        if bounty_id not in bounties_db:
            raise HTTPException(status_code=404, detail="Bounty not found")
        
        return {
            "status": "success",
            "bounty": bounties_db[bounty_id]
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching bounty: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/bounties/{bounty_id}/bid")
async def place_bid(bounty_id: str, request: BidRequest):
    """Place a bid on a bounty"""
    try:
        if bounty_id not in bounties_db:
            raise HTTPException(status_code=404, detail="Bounty not found")
        
        bid_id = f"bid_{len(bids_db) + 1}"
        bid = {
            "bid_id": bid_id,
            "bounty_id": bounty_id,
            "channel_owner_id": request.channel_owner_id,
            "channel_id": request.channel_id,
            "status": "pending",
            "created_at": datetime.utcnow().isoformat()
        }
        bids_db[bid_id] = bid
        
        logger.info(f"Bid placed: {bid_id} on bounty {bounty_id}")
        return {
            "status": "success",
            "message": "Bid placed",
            "bid": bid
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Bid placement error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/bounties/{bounty_id}/confirm-views")
async def confirm_views(bounty_id: str, request: ConfirmViewsRequest):
    """Confirm views and trigger payout"""
    try:
        if bounty_id not in bounties_db:
            raise HTTPException(status_code=404, detail="Bounty not found")
        
        bounty = bounties_db[bounty_id]
        
        # Update bounty status
        bounty["status"] = "confirmed"
        bounties_db[bounty_id] = bounty
        
        # Create transaction record
        tx_id = f"tx_{len(transactions_db) + 1}"
        transaction = Transaction(
            tx_id=tx_id,
            from_user=bounty["advertiser_id"],
            to_user=request.channel_owner_id,
            amount=bounty["ton_amount"],
            tx_type="payout",
            status="success",
            bounty_id=bounty_id,
            created_at=datetime.utcnow()
        )
        transactions_db[tx_id] = transaction.model_dump()
        
        logger.info(f"Views confirmed for bounty {bounty_id}, payout triggered")
        return {
            "status": "success",
            "message": "Views confirmed, payout released",
            "bounty": bounty,
            "transaction": transaction.model_dump()
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Confirm views error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/transactions/{user_id}")
async def get_transactions(user_id: int):
    """Get transaction history for a user"""
    try:
        user_txs = [tx for tx in transactions_db.values() 
                    if tx.get("from_user") == user_id or tx.get("to_user") == user_id]
        
        return {
            "status": "success",
            "count": len(user_txs),
            "transactions": user_txs
        }
    except Exception as e:
        logger.error(f"Error fetching transactions: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/bot/post-ad")
async def post_ad(bounty_id: str, channel_id: int):
    """Trigger bot to post ad to channel (called by backend job)"""
    try:
        if bounty_id not in bounties_db:
            raise HTTPException(status_code=404, detail="Bounty not found")
        
        bounty = bounties_db[bounty_id]
        
        # Update bounty status to posted
        bounty["status"] = "posted"
        bounties_db[bounty_id] = bounty
        
        logger.info(f"Ad posted to channel {channel_id} for bounty {bounty_id}")
        return {
            "status": "success",
            "message": "Ad posted to channel",
            "bounty_id": bounty_id,
            "channel_id": channel_id
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Post ad error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/")
async def root():
    """Root endpoint with API documentation"""
    return {
        "name": "AdBounty API",
        "version": "1.0.0",
        "description": "Telegram Mini App for Ad Marketplace with TON Escrow",
        "docs": "/docs",
        "endpoints": {
            "health": "/health",
            "auth": "/auth/telegram",
            "channels": "/channels/verified",
            "bounties": "/bounties/create",
            "transactions": "/transactions/{user_id}"
        }
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
