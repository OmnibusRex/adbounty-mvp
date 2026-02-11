import { useState, useCallback } from 'react';
import { apiClient } from '@/lib/api';
import { Bounty, CreateBountyForm } from '@/types';

export function useBounties() {
  const [bounties, setBounties] = useState<Bounty[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const createBounty = useCallback(async (data: CreateBountyForm & { advertiser_id: number }) => {
    setIsLoading(true);
    setError(null);
    try {
      const response = await apiClient.bounties.create(data);
      const newBounty = response.data.bounty;
      setBounties((prev) => [...prev, newBounty]);
      return newBounty;
    } catch (err: any) {
      const errorMessage = err.response?.data?.detail || 'Failed to create bounty';
      setError(errorMessage);
      throw err;
    } finally {
      setIsLoading(false);
    }
  }, []);

  const getBounty = useCallback(async (bountyId: string) => {
    setIsLoading(true);
    setError(null);
    try {
      const response = await apiClient.bounties.get(bountyId);
      return response.data.bounty;
    } catch (err: any) {
      const errorMessage = err.response?.data?.detail || 'Failed to fetch bounty';
      setError(errorMessage);
      throw err;
    } finally {
      setIsLoading(false);
    }
  }, []);

  const placeBid = useCallback(async (bountyId: string, channelOwnerId: number, channelId: number) => {
    setIsLoading(true);
    setError(null);
    try {
      const response = await apiClient.bounties.bid(bountyId, {
        bounty_id: bountyId,
        channel_owner_id: channelOwnerId,
        channel_id: channelId,
      });
      return response.data.bid;
    } catch (err: any) {
      const errorMessage = err.response?.data?.detail || 'Failed to place bid';
      setError(errorMessage);
      throw err;
    } finally {
      setIsLoading(false);
    }
  }, []);

  const confirmViews = useCallback(async (bountyId: string, channelOwnerId: number, proofUrl?: string) => {
    setIsLoading(true);
    setError(null);
    try {
      const response = await apiClient.bounties.confirmViews(bountyId, {
        bounty_id: bountyId,
        channel_owner_id: channelOwnerId,
        proof_url: proofUrl,
      });
      return response.data;
    } catch (err: any) {
      const errorMessage = err.response?.data?.detail || 'Failed to confirm views';
      setError(errorMessage);
      throw err;
    } finally {
      setIsLoading(false);
    }
  }, []);

  return {
    bounties,
    isLoading,
    error,
    createBounty,
    getBounty,
    placeBid,
    confirmViews,
  };
}
