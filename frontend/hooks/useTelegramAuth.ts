import { useState, useEffect, useCallback } from 'react';
import { apiClient } from '@/lib/api';
import { User } from '@/types';

export function useTelegramAuth() {
  const [user, setUser] = useState<User | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  // Check if user is already authenticated
  useEffect(() => {
    const checkAuth = async () => {
      try {
        const storedUser = localStorage.getItem('user');
        if (storedUser) {
          const parsedUser = JSON.parse(storedUser);
          setUser(parsedUser);
          setIsAuthenticated(true);
        }
      } catch (err) {
        console.error('Failed to restore user session:', err);
      }
    };

    checkAuth();
  }, []);

  const authenticate = useCallback(async (telegramId: number, username: string) => {
    setIsLoading(true);
    setError(null);

    try {
      const response = await apiClient.auth.telegram(telegramId, username);
      const userData = response.data.user;

      setUser(userData);
      setIsAuthenticated(true);

      // Store user in localStorage
      localStorage.setItem('user', JSON.stringify(userData));
      localStorage.setItem('auth_token', `telegram_${telegramId}`);

      return userData;
    } catch (err: any) {
      const errorMessage = err.response?.data?.detail || 'Authentication failed';
      setError(errorMessage);
      throw err;
    } finally {
      setIsLoading(false);
    }
  }, []);

  const logout = useCallback(() => {
    setUser(null);
    setIsAuthenticated(false);
    localStorage.removeItem('user');
    localStorage.removeItem('auth_token');
  }, []);

  return {
    user,
    isLoading,
    error,
    isAuthenticated,
    authenticate,
    logout,
  };
}
