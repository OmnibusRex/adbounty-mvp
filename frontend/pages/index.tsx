import React, { useEffect, useState } from 'react';
import Head from 'next/head';
import Link from 'next/link';

export default function Home() {
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    setIsLoading(false);
  }, []);

  if (isLoading) {
    return (
      <div className="flex items-center justify-center min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
          <p className="text-gray-600">Loading AdBounty...</p>
        </div>
      </div>
    );
  }

  return (
    <>
      <Head>
        <title>AdBounty - Ad Marketplace for Telegram</title>
        <meta name="description" content="Monetize your Telegram channel with AdBounty" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
        {/* Navigation */}
        <nav className="bg-white shadow-sm sticky top-0 z-50">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex justify-between items-center h-16">
              <div className="flex items-center gap-2">
                <div className="w-8 h-8 bg-gradient-to-br from-blue-600 to-indigo-600 rounded-lg flex items-center justify-center">
                  <span className="text-white font-bold text-lg">🎯</span>
                </div>
                <span className="text-xl font-bold text-gray-900">AdBounty</span>
              </div>
              <div className="hidden md:flex gap-8">
                <a href="#features" className="text-gray-600 hover:text-gray-900">Features</a>
                <a href="#how-it-works" className="text-gray-600 hover:text-gray-900">How It Works</a>
                <a href="#pricing" className="text-gray-600 hover:text-gray-900">Pricing</a>
              </div>
              <button className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded-lg font-medium transition">
                Launch App
              </button>
            </div>
          </div>
        </nav>

        {/* Hero Section */}
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
          <div className="grid md:grid-cols-2 gap-12 items-center">
            <div>
              <h1 className="text-5xl md:text-6xl font-bold text-gray-900 mb-6">
                Monetize Your Telegram Channel
              </h1>
              <p className="text-xl text-gray-600 mb-8">
                AdBounty connects advertisers with Telegram channel owners. Create bounties, earn TON, and grow your audience.
              </p>
              <div className="flex gap-4">
                <button className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 rounded-lg font-medium transition text-lg">
                  Get Started
                </button>
                <button className="border-2 border-gray-300 text-gray-900 px-8 py-3 rounded-lg font-medium hover:border-gray-400 transition text-lg">
                  Learn More
                </button>
              </div>
            </div>
            <div className="bg-white rounded-2xl shadow-xl p-8">
              <div className="space-y-4">
                <div className="flex items-center gap-4">
                  <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center">
                    <span className="text-2xl">📱</span>
                  </div>
                  <div>
                    <h3 className="font-semibold text-gray-900">Telegram Native</h3>
                    <p className="text-sm text-gray-600">Mini App integrated directly in Telegram</p>
                  </div>
                </div>
                <div className="flex items-center gap-4">
                  <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center">
                    <span className="text-2xl">💰</span>
                  </div>
                  <div>
                    <h3 className="font-semibold text-gray-900">TON Payments</h3>
                    <p className="text-sm text-gray-600">Secure escrow powered by TON blockchain</p>
                  </div>
                </div>
                <div className="flex items-center gap-4">
                  <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center">
                    <span className="text-2xl">⚡</span>
                  </div>
                  <div>
                    <h3 className="font-semibold text-gray-900">Instant Payouts</h3>
                    <p className="text-sm text-gray-600">Receive earnings instantly to your wallet</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Features Section */}
        <section id="features" className="bg-white py-20">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <h2 className="text-4xl font-bold text-center text-gray-900 mb-16">Features</h2>
            <div className="grid md:grid-cols-3 gap-8">
              {[
                {
                  icon: '📊',
                  title: 'Verified Channels',
                  description: 'Access only verified, high-quality Telegram channels'
                },
                {
                  icon: '🎯',
                  title: 'Targeted Campaigns',
                  description: 'Create bounties for specific niches and audiences'
                },
                {
                  icon: '✅',
                  title: 'Smart Escrow',
                  description: 'Secure payments with automatic confirmation'
                },
                {
                  icon: '📈',
                  title: 'Analytics',
                  description: 'Track campaign performance and ROI'
                },
                {
                  icon: '🔐',
                  title: 'Secure',
                  description: 'Blockchain-backed security and transparency'
                },
                {
                  icon: '⚙️',
                  title: 'Easy Setup',
                  description: 'No coding required, simple intuitive interface'
                }
              ].map((feature, idx) => (
                <div key={idx} className="p-8 border border-gray-200 rounded-xl hover:shadow-lg transition">
                  <div className="text-4xl mb-4">{feature.icon}</div>
                  <h3 className="text-xl font-semibold text-gray-900 mb-2">{feature.title}</h3>
                  <p className="text-gray-600">{feature.description}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* How It Works Section */}
        <section id="how-it-works" className="py-20 bg-gradient-to-br from-blue-50 to-indigo-100">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <h2 className="text-4xl font-bold text-center text-gray-900 mb-16">How It Works</h2>
            <div className="grid md:grid-cols-4 gap-8">
              {[
                { step: '1', title: 'Create', desc: 'Create a bounty with TON payment' },
                { step: '2', title: 'Select', desc: 'Choose target channels' },
                { step: '3', title: 'Post', desc: 'Ad posted automatically' },
                { step: '4', title: 'Earn', desc: 'Receive payout instantly' }
              ].map((item, idx) => (
                <div key={idx} className="text-center">
                  <div className="w-16 h-16 bg-blue-600 text-white rounded-full flex items-center justify-center text-2xl font-bold mx-auto mb-4">
                    {item.step}
                  </div>
                  <h3 className="text-xl font-semibold text-gray-900 mb-2">{item.title}</h3>
                  <p className="text-gray-600">{item.desc}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* CTA Section */}
        <section className="bg-blue-600 text-white py-20">
          <div className="max-w-4xl mx-auto text-center px-4">
            <h2 className="text-4xl font-bold mb-6">Ready to Get Started?</h2>
            <p className="text-xl mb-8 text-blue-100">
              Join thousands of Telegram channel owners earning TON with AdBounty
            </p>
            <button className="bg-white text-blue-600 px-8 py-3 rounded-lg font-semibold hover:bg-blue-50 transition text-lg">
              Launch AdBounty
            </button>
          </div>
        </section>

        {/* Footer */}
        <footer className="bg-gray-900 text-gray-400 py-12">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="grid md:grid-cols-4 gap-8 mb-8">
              <div>
                <h3 className="text-white font-semibold mb-4">AdBounty</h3>
                <p className="text-sm">Monetize your Telegram channel with AdBounty</p>
              </div>
              <div>
                <h4 className="text-white font-semibold mb-4">Product</h4>
                <ul className="space-y-2 text-sm">
                  <li><a href="#" className="hover:text-white">Features</a></li>
                  <li><a href="#" className="hover:text-white">Pricing</a></li>
                  <li><a href="#" className="hover:text-white">Security</a></li>
                </ul>
              </div>
              <div>
                <h4 className="text-white font-semibold mb-4">Company</h4>
                <ul className="space-y-2 text-sm">
                  <li><a href="#" className="hover:text-white">About</a></li>
                  <li><a href="#" className="hover:text-white">Blog</a></li>
                  <li><a href="#" className="hover:text-white">Contact</a></li>
                </ul>
              </div>
              <div>
                <h4 className="text-white font-semibold mb-4">Legal</h4>
                <ul className="space-y-2 text-sm">
                  <li><a href="#" className="hover:text-white">Privacy</a></li>
                  <li><a href="#" className="hover:text-white">Terms</a></li>
                  <li><a href="#" className="hover:text-white">Cookies</a></li>
                </ul>
              </div>
            </div>
            <div className="border-t border-gray-800 pt-8 text-center text-sm">
              <p>&copy; 2024 AdBounty. All rights reserved.</p>
            </div>
          </div>
        </footer>
      </main>
    </>
  );
}
