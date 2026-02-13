# Submissão - AdBounty MVP

## 🎯 Visão Geral
AdBounty é um marketplace descentralizado de anúncios para canais do Telegram, usando TON para pagamentos em escrow.

## ✅ Funcionalidades Implementadas
- Bot Telegram funcional (@AdEscrowMVPBot)
- Backend FastAPI com documentação Swagger
- Mini App Telegram básico
- Deploy profissional no Railway
- Integração com python-telegram-bot
- Sistema de escrow via contratos TON

## 🏗️ Arquitetura
- **Backend**: FastAPI + Uvicorn
- **Bot**: python-telegram-bot 20.7
- **Frontend**: HTML/CSS/JS puro (Mini App)
- **Infra**: Railway (Nixpacks + Docker)

## 🚀 Deploy
- URL: https://adbounty-mvp-production.up.railway.app
- Bot: @AdEscrowMVPBot

## 🔮 Próximos Passos
- Implementar verificação de stats de canal
- Criar fluxo completo de aprovação criativa
- Adicionar auto-posting verificado
- Implementar timeout automático para deals inativas

## 📊 Decisões Técnicas
- Usei python-telegram-bot em vez de aiogram por estabilidade
- Docker + Nixpacks para deploy flexível
- Railway para hospedagem (gratuito e fácil)

## ⚠️ Limitações Conhecidas
- Mini App ainda básico (sem funcionalidades completas)
- Verificação de stats via fallback apenas
- Fluxo de aprovação simplificado
