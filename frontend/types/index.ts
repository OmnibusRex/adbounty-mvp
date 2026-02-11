// User types
export interface User {
  telegram_id: number;
  username: string;
  wallet_address?: string;
  created_at?: string;
}

// Channel types
export interface Channel {
  channel_id: number;
  channel_name: string;
  subscribers: number;
  niche: string;
  verified: boolean;
  owner_id: number;
  created_at?: string;
}

// Bounty types
export interface Bounty {
  bounty_id: string;
  advertiser_id: number;
  ton_amount: number;
  ad_text: string;
  ad_link: string;
  target_channels: number[];
  status: 'pending' | 'posted' | 'confirmed' | 'completed' | 'cancelled';
  escrow_address?: string;
  created_at?: string;
  deadline?: string;
}

// Bid types
export interface Bid {
  bid_id: string;
  bounty_id: string;
  channel_owner_id: number;
  channel_id: number;
  status: 'pending' | 'accepted' | 'rejected' | 'completed';
  created_at?: string;
}

// Deal types (accepted bid)
export interface Deal {
  deal_id: string;
  bounty_id: string;
  advertiser_id: number;
  channel_owner_id: number;
  channel_id: number;
  amount: number;
  status: 'posted' | 'awaiting_confirmation' | 'confirmed' | 'completed';
  created_at?: string;
  confirmed_at?: string;
}

// Transaction types
export interface Transaction {
  tx_id: string;
  from_user: number;
  to_user: number;
  amount: number;
  tx_type: 'deposit' | 'payout' | 'refund';
  status: 'pending' | 'success' | 'failed';
  bounty_id?: string;
  tx_hash?: string;
  created_at?: string;
}

// API Response types
export interface ApiResponse<T> {
  status: 'success' | 'error';
  message?: string;
  data?: T;
  error?: string;
}

// Form types
export interface CreateBountyForm {
  ton_amount: number;
  ad_text: string;
  ad_link: string;
  target_channels: number[];
  deadline_days: number;
}

export interface BidForm {
  bounty_id: string;
  channel_owner_id: number;
  channel_id: number;
}

export interface ConfirmViewsForm {
  bounty_id: string;
  channel_owner_id: number;
  proof_url?: string;
}

// UI State types
export interface LoadingState {
  isLoading: boolean;
  error?: string;
}

export interface ToastMessage {
  id: string;
  type: 'success' | 'error' | 'info' | 'warning';
  message: string;
  duration?: number;
}

// Telegram types
export interface TelegramUser {
  id: number;
  is_bot: boolean;
  first_name: string;
  last_name?: string;
  username?: string;
  language_code?: string;
}

// TON Connect types
export interface TonConnectUI {
  connected: boolean;
  account?: {
    address: string;
    chain: string;
    publicKey: string;
  };
  connect(): Promise<void>;
  disconnect(): Promise<void>;
  sendTransaction(tx: any): Promise<any>;
}

// Pagination types
export interface PaginationParams {
  page: number;
  limit: number;
  sort?: string;
  order?: 'asc' | 'desc';
}

export interface PaginatedResponse<T> {
  items: T[];
  total: number;
  page: number;
  limit: number;
  pages: number;
}
