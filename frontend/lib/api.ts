import axios, { AxiosInstance } from 'axios';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

// Create axios instance
const api: AxiosInstance = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add token to requests if available
api.interceptors.request.use((config) => {
  if (typeof window !== 'undefined') {
    const token = localStorage.getItem('auth_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
  }
  return config;
});

// Handle errors
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Handle unauthorized
      if (typeof window !== 'undefined') {
        localStorage.removeItem('auth_token');
        window.location.href = '/';
      }
    }
    return Promise.reject(error);
  }
);

// API Methods
export const apiClient = {
  // Auth
  auth: {
    telegram: (telegramId: number, username: string) =>
      api.post('/auth/telegram', null, { params: { telegram_id: telegramId, username } }),
  },

  // Channels
  channels: {
    getVerified: () => api.get('/channels/verified'),
    verify: (channelId: number, channelName: string, ownerId: number, subscribers: number, niche: string) =>
      api.post('/channels/verify', null, {
        params: { channel_id: channelId, channel_name: channelName, owner_id: ownerId, subscribers, niche },
      }),
  },

  // Bounties
  bounties: {
    create: (data: {
      advertiser_id: number;
      ton_amount: number;
      ad_text: string;
      ad_link: string;
      target_channels: number[];
      deadline_days?: number;
    }) => api.post('/bounties/create', data),

    get: (bountyId: string) => api.get(`/bounties/${bountyId}`),

    bid: (bountyId: string, data: { bounty_id: string; channel_owner_id: number; channel_id: number }) =>
      api.post(`/bounties/${bountyId}/bid`, data),

    confirmViews: (bountyId: string, data: { bounty_id: string; channel_owner_id: number; proof_url?: string }) =>
      api.post(`/bounties/${bountyId}/confirm-views`, data),
  },

  // Transactions
  transactions: {
    getHistory: (userId: number) => api.get(`/transactions/${userId}`),
  },

  // Bot
  bot: {
    postAd: (bountyId: string, channelId: number) =>
      api.post('/bot/post-ad', null, { params: { bounty_id: bountyId, channel_id: channelId } }),
  },
};

export default api;
