import { useState, useCallback, useEffect } from 'react';
import { useTonConnectUI } from '@tonconnect/ui-react';

export function useTonConnect() {
  const [tonConnectUI] = useTonConnectUI();
  const [isConnected, setIsConnected] = useState(false);
  const [walletAddress, setWalletAddress] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Check connection status
  useEffect(() => {
    const checkConnection = async () => {
      try {
        if (tonConnectUI.account) {
          setIsConnected(true);
          setWalletAddress(tonConnectUI.account.address);
        } else {
          setIsConnected(false);
          setWalletAddress(null);
        }
      } catch (err) {
        console.error('Failed to check TON Connect status:', err);
      }
    };

    checkConnection();
  }, [tonConnectUI.account]);

  const connect = useCallback(async () => {
    setIsLoading(true);
    setError(null);

    try {
      await tonConnectUI.openModal();
      if (tonConnectUI.account) {
        setIsConnected(true);
        setWalletAddress(tonConnectUI.account.address);
      }
    } catch (err: any) {
      const errorMessage = err.message || 'Failed to connect wallet';
      setError(errorMessage);
      throw err;
    } finally {
      setIsLoading(false);
    }
  }, [tonConnectUI]);

  const disconnect = useCallback(async () => {
    setIsLoading(true);
    setError(null);

    try {
      await tonConnectUI.disconnect();
      setIsConnected(false);
      setWalletAddress(null);
    } catch (err: any) {
      const errorMessage = err.message || 'Failed to disconnect wallet';
      setError(errorMessage);
      throw err;
    } finally {
      setIsLoading(false);
    }
  }, [tonConnectUI]);

  const sendTransaction = useCallback(
    async (transaction: any) => {
      setIsLoading(true);
      setError(null);

      try {
        const result = await tonConnectUI.sendTransaction(transaction);
        return result;
      } catch (err: any) {
        const errorMessage = err.message || 'Failed to send transaction';
        setError(errorMessage);
        throw err;
      } finally {
        setIsLoading(false);
      }
    },
    [tonConnectUI]
  );

  return {
    isConnected,
    walletAddress,
    isLoading,
    error,
    connect,
    disconnect,
    sendTransaction,
    tonConnectUI,
  };
}
