import React, { useEffect } from 'react';
import type { AppProps } from 'next/app';
import { TonConnectUIProvider } from '@tonconnect/ui-react';
import { initData, useSignal } from '@telegram-apps/sdk-react';
import '../styles/globals.css';

const manifestUrl = process.env.NEXT_PUBLIC_TON_CONNECT_MANIFEST_URL || 'https://adbounty.app/tonconnect-manifest.json';

function MyApp({ Component, pageProps }: AppProps) {
  const isDev = process.env.NODE_ENV === 'development';
  const [isReady, setIsReady] = React.useState(false);

  useEffect(() => {
    // Initialize Telegram SDK
    try {
      initData.restore();
      setIsReady(true);
    } catch (e) {
      if (isDev) {
        console.warn('Failed to restore Telegram init data:', e);
      }
      setIsReady(true);
    }
  }, []);

  if (!isReady) {
    return <div>Loading...</div>;
  }

  return (
    <TonConnectUIProvider manifestUrl={manifestUrl}>
      <Component {...pageProps} />
    </TonConnectUIProvider>
  );
}

export default MyApp;
