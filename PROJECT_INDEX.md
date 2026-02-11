# AdBounty - Project Index

Índice completo de todos os arquivos e componentes do projeto.

## 📊 Estatísticas do Projeto

- Backend Python: 939 linhas de código
- Frontend TypeScript: 759 linhas de código
- Contratos TON FunC: 142 linhas de código
- Documentação: 1860 linhas
- Total: ~3700 linhas de código

## 📁 Estrutura de Diretórios

```
adbounty/
├── backend/                          # FastAPI Backend
│   ├── main.py                      # API principal com 15+ endpoints
│   ├── bot.py                       # Bot Telegram com aiogram
│   ├── test_api.py                  # Testes unitários
│   ├── requirements.txt             # Dependências Python
│   ├── Dockerfile                   # Imagem Docker para backend
│   └── migrations/                  # Migrações de banco de dados
│
├── frontend/                         # Next.js Frontend
│   ├── pages/
│   │   ├── _app.tsx                # App wrapper com providers
│   │   └── index.tsx               # Landing page
│   ├── lib/
│   │   └── api.ts                  # Cliente HTTP para API
│   ├── types/
│   │   └── index.ts                # Tipos TypeScript
│   ├── hooks/
│   │   ├── useBounties.ts          # Hook para gerenciar bounties
│   │   ├── useTelegramAuth.ts      # Hook para autenticação
│   │   └── useTonConnect.ts        # Hook para TON Connect
│   ├── styles/
│   │   └── globals.css             # Estilos globais
│   ├── public/
│   │   └── tonconnect-manifest.json # Manifest TON Connect
│   ├── package.json                # Dependências Node.js
│   ├── tsconfig.json               # Configuração TypeScript
│   └── next.config.js              # Configuração Next.js
│
├── contracts/                        # TON Smart Contracts
│   ├── escrow.fc                   # Contrato de escrow (142 linhas)
│   └── deploy.sh                   # Script de deploy
│
├── .github/
│   └── workflows/
│       └── deploy.yml              # CI/CD com GitHub Actions
│
├── Documentação/
│   ├── README.md                   # Documentação principal (8.9 KB)
│   ├── EXECUTIVE_SUMMARY.md        # Resumo executivo
│   ├── ROADMAP.md                  # Plano de 5 fases (6.3 KB)
│   ├── SETUP.md                    # Guia de setup local (5.9 KB)
│   ├── DEPLOYMENT.md               # Guia de deployment (6.4 KB)
│   ├── DEMO_SCRIPT.md              # Roteiro de vídeo de 1 minuto (4.9 KB)
│   ├── design.md                   # Plano de design (5.9 KB)
│   └── todo.md                     # Tarefas do projeto (3.7 KB)
│
├── Configuração/
│   ├── docker-compose.yml          # Orquestração de containers
│   ├── vercel.json                 # Configuração Vercel
│   ├── railway.toml                # Configuração Railway
│   ├── Makefile                    # Automação de tarefas
│   ├── .gitignore_adbounty         # Arquivos ignorados
│   └── .env.example                # Variáveis de ambiente
│
└── Arquivos Raiz/
    ├── package.json                # Dependências root
    ├── tsconfig.json               # Configuração TypeScript root
    └── PROJECT_INDEX.md            # Este arquivo
```

## 🔑 Arquivos Principais

### Backend

| Arquivo | Linhas | Descrição |
|---------|--------|-----------|
| main.py | 450 | API FastAPI com endpoints |
| bot.py | 280 | Bot Telegram com aiogram |
| test_api.py | 209 | Testes unitários |

### Frontend

| Arquivo | Linhas | Descrição |
|---------|--------|-----------|
| pages/_app.tsx | 30 | App wrapper |
| pages/index.tsx | 200 | Landing page |
| lib/api.ts | 80 | Cliente HTTP |
| types/index.ts | 150 | Tipos TypeScript |
| hooks/useBounties.ts | 120 | Hook de bounties |
| hooks/useTelegramAuth.ts | 70 | Hook de autenticação |
| hooks/useTonConnect.ts | 90 | Hook de TON Connect |

### Contratos

| Arquivo | Linhas | Descrição |
|---------|--------|-----------|
| escrow.fc | 142 | Smart contract de escrow |
| deploy.sh | 80 | Script de deploy |

### Documentação

| Arquivo | Tamanho | Descrição |
|---------|---------|-----------|
| README.md | 8.9 KB | Documentação completa |
| ROADMAP.md | 6.3 KB | Plano de 5 fases |
| SETUP.md | 5.9 KB | Guia de setup |
| DEPLOYMENT.md | 6.4 KB | Guia de deployment |
| DEMO_SCRIPT.md | 4.9 KB | Roteiro de vídeo |
| design.md | 5.9 KB | Plano de design |

## 🚀 Como Começar

1. Leia EXECUTIVE_SUMMARY.md para visão geral
2. Siga SETUP.md para setup local
3. Consulte README.md para arquitetura
4. Veja DEPLOYMENT.md para produção
5. Revise ROADMAP.md para futuro

## 📦 Dependências Principais

### Backend
- FastAPI 0.104.1
- aiogram 3.3.0
- SQLAlchemy 2.0.23
- PostgreSQL 14

### Frontend
- Next.js 14.0.0
- React 18.2.0
- TypeScript 5.0.0
- @telegram-apps/sdk 0.3.0
- @tonconnect/ui-react 2.0.0

### Contratos
- TON FunC compiler
- tonpy 0.2.0

## 🔐 Variáveis de Ambiente

Veja .env.example para lista completa de variáveis necessárias:
- BOT_TOKEN (Telegram)
- DATABASE_URL (PostgreSQL)
- TON_API_KEY (TON)
- JWT_SECRET (Segurança)

## 📊 Endpoints da API

### Autenticação
- POST /auth/telegram

### Canais
- GET /channels/verified
- POST /channels/verify

### Bounties
- POST /bounties/create
- GET /bounties/{id}
- POST /bounties/{id}/bid
- POST /bounties/{id}/confirm-views

### Transações
- GET /transactions/{user_id}

### Bot
- POST /bot/post-ad

## 🧪 Testes

Backend testes em backend/test_api.py:
- TestHealth
- TestAuthentication
- TestChannels
- TestBounties
- TestBids
- TestConfirmViews
- TestTransactions
- TestBotEndpoints

## 📱 Telas Frontend

1. Splash/Onboarding
2. Login Telegram
3. Catálogo de Canais
4. Detalhes do Canal
5. Criar Bounty
6. Meus Bounties
7. Detalhes da Bounty
8. Bid/Escrow
9. Meus Deals
10. Confirmar Views
11. Histórico de Transações
12. Perfil/Configurações

## 🎯 Fluxo Principal

1. Login Telegram → Autenticação
2. Catálogo → Listar canais verificados
3. Criar Bounty → Form com TON amount
4. TON Connect → Depositar em escrow
5. Auto-Post → Bot publica no canal
6. Confirmar Views → Owner confirma
7. Payout → Contrato libera TON

## 🚢 Deployment

- Frontend: Vercel
- Backend: Railway
- Banco de Dados: PostgreSQL (Railway)
- Smart Contract: TON Testnet
- Bot: Railway Worker

## 📚 Recursos Externos

- Telegram Bot API: https://core.telegram.org/bots
- TON Documentation: https://ton.org/docs
- FastAPI: https://fastapi.tiangolo.com
- Next.js: https://nextjs.org/docs
- aiogram: https://docs.aiogram.dev

## ✅ Checklist de Implementação

- [x] Backend FastAPI com endpoints
- [x] Bot Telegram com aiogram
- [x] Contrato TON FunC
- [x] Frontend Next.js
- [x] Hooks customizados
- [x] Tipos TypeScript
- [x] Documentação completa
- [x] Docker Compose
- [x] GitHub Actions CI/CD
- [x] Testes unitários
- [x] Scripts de deploy
- [x] Makefile
- [ ] Testes end-to-end
- [ ] Performance optimization
- [ ] Monitoring setup

## 🎓 Aprendizados

Este projeto demonstra:
- Integração de Telegram SDK
- Smart contracts em TON FunC
- FastAPI para APIs escaláveis
- Next.js para frontend moderno
- Docker para containerização
- CI/CD com GitHub Actions
- Deployment em Vercel e Railway

## 📞 Suporte

Para dúvidas ou problemas:
1. Consulte a documentação relevante
2. Verifique os logs do Docker
3. Abra uma issue no GitHub
4. Entre em contato via email

---

**Versão**: 1.0.0-alpha
**Última atualização**: 11 de Fevereiro de 2024
**Status**: Pronto para Contest
