# AdBounty - Project TODO

## Frontend (Next.js + Telegram SDK + TON Connect)
- [ ] Setup Next.js project structure (pages, components, lib)
- [ ] Implement Telegram SDK integration (@telegram-apps/sdk)
- [ ] Create Telegram login/authentication flow
- [ ] Implement TON Connect UI (@tonconnect/ui-react)
- [ ] Build Catalog screen (list verified channels)
- [ ] Build Channel Details screen
- [ ] Build Create Bounty form (TON amount, ad text, link, target channels)
- [ ] Build Bounty Details screen
- [ ] Build My Bounties screen (with tabs: Active/Completed)
- [ ] Build Bid/Escrow confirmation screen (TON Connect deposit)
- [ ] Build My Deals screen (for channel owners)
- [ ] Build Confirm Views screen (owner confirmation)
- [ ] Build Transaction History screen
- [ ] Build Profile/Settings screen
- [ ] Implement responsive design (mobile-first)
- [ ] Add dark mode support
- [ ] Setup environment variables (.env.example)
- [ ] Create UI Kit components (Button, Card, Input, etc.)

## Backend (FastAPI + aiogram)
- [ ] Setup FastAPI project structure
- [ ] Create database models (User, Channel, Bounty, Deal, Transaction)
- [ ] Implement Telegram verification endpoint (/verify-channel)
- [ ] Implement create bounty endpoint (/create-bounty)
- [ ] Implement bid acceptance endpoint (/accept-bid)
- [ ] Implement post ad endpoint (/post-ad)
- [ ] Implement confirm views endpoint (/confirm-views)
- [ ] Implement transaction history endpoint (/transactions)
- [ ] Setup aiogram bot for auto-posting
- [ ] Implement Bot.sendMessage integration
- [ ] Create TON escrow interaction layer
- [ ] Setup database migrations
- [ ] Implement error handling and logging
- [ ] Create API documentation (OpenAPI/Swagger)

## TON Smart Contracts (FunC)
- [ ] Create escrow contract (escrow.fc)
- [ ] Implement deposit function
- [ ] Implement confirm function (owner confirms views)
- [ ] Implement release function (payout to owner)
- [ ] Implement refund function (if deal cancelled)
- [ ] Deploy to TON testnet
- [ ] Create deployment script (deploy.sh)
- [ ] Test contract locally with TonWeb

## Documentation & Configuration
- [ ] Create comprehensive README.md
- [ ] Create ROADMAP.md (AI matching, disputes, multi-channel, Stars rev-share)
- [ ] Create API documentation
- [ ] Create deployment guide
- [ ] Create .env.example with all required variables
- [ ] Create vercel.json (Vercel deployment config)
- [ ] Create Railway.toml (Railway deployment config)
- [ ] Create docker-compose.yml (local development)
- [ ] Create demo video script (1 min)
- [ ] Generate architecture diagram

## Testing & Quality
- [ ] Setup unit tests (frontend)
- [ ] Setup integration tests (backend)
- [ ] Test Telegram login flow
- [ ] Test TON Connect integration
- [ ] Test bounty creation flow end-to-end
- [ ] Test bid acceptance flow
- [ ] Test auto-posting to Telegram channel
- [ ] Test escrow deposit/release
- [ ] Test transaction history
- [ ] Manual testing on mobile (iOS/Android)

## Branding & Assets
- [ ] Generate AdBounty logo/icon
- [ ] Create splash screen
- [ ] Create favicon
- [ ] Create Android adaptive icon
- [ ] Update app.config.ts with branding

## Deployment & DevOps
- [ ] Setup Vercel deployment (frontend)
- [ ] Setup Railway deployment (backend)
- [ ] Setup TON testnet deployment
- [ ] Create CI/CD pipeline (GitHub Actions)
- [ ] Setup monitoring and logging
- [ ] Create backup strategy

## Final Delivery
- [ ] Create ZIP package with all files
- [ ] Prepare GitHub-ready structure
- [ ] Generate deploy links (Vercel + Railway)
- [ ] Create screenshots for README
- [ ] Record 1-minute demo video
- [ ] Final code review and cleanup
