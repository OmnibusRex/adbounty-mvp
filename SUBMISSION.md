# Submission - AdBounty MVP

## 🎯 Overview
AdBounty is a decentralized advertisement marketplace for Telegram channels, using TON for escrow payments.

## ✅ Implemented Features
- Functional Telegram Bot (@AdEscrowMVPBot)
- FastAPI backend with Swagger documentation
- Basic Telegram Mini App
- Professional deployment on Railway
- Integration with python-telegram-bot
- Escrow system via TON contracts

## 🏗️ Architecture
- **Backend**: FastAPI + Uvicorn
- **Bot**: python-telegram-bot 20.7
- **Frontend**: Pure HTML/CSS/JS (Mini App)
- **Infra**: Railway (Nixpacks + Docker)

## 🚀 Deployment
- URL: https://adbounty-mvp-production.up.railway.app
- Bot: @AdEscrowMVPBot

## 🔮 Next Steps
- Implement channel stats verification (TGStat API)
- Create complete creative approval flow
- Add verified auto-posting
- Implement automatic timeout for inactive deals

## 📊 Technical Decisions
- Chose python-telegram-bot over aiogram for stability
- Docker + Nixpacks for flexible deployment
- Railway for hosting (free and easy to use)

## ⚠️ Known Limitations
- Mini App still basic (no complete features yet)
- Stats verification via fallback only
- Simplified approval flow
