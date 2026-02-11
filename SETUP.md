# AdBounty - Setup Guide

Guia completo para configurar e executar o AdBounty localmente.

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- **Node.js** 18+ (https://nodejs.org)
- **Python** 3.11+ (https://www.python.org)
- **Docker** e **Docker Compose** (https://www.docker.com)
- **Git** (https://git-scm.com)
- **Make** (opcional, para usar Makefile)

## 🚀 Quick Start (Docker)

A forma mais rápida de começar é usando Docker Compose:

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/adbounty.git
cd adbounty

# Copie o arquivo de ambiente
cp .env.example .env

# Edite as variáveis de ambiente necessárias
nano .env

# Inicie os serviços
docker-compose up -d

# Aguarde os serviços iniciarem (30-60 segundos)
docker-compose logs -f
```

Acesse:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- PostgreSQL: localhost:5432

## 💻 Setup Local (Sem Docker)

### 1. Setup Backend

```bash
# Navegue para o diretório backend
cd backend

# Crie um ambiente virtual Python
python -m venv venv

# Ative o ambiente virtual
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Instale as dependências
pip install -r requirements.txt

# Configure o banco de dados
# Certifique-se de que PostgreSQL está rodando
# Crie um banco de dados chamado 'adbounty'
createdb adbounty

# Inicie o servidor FastAPI
python main.py
```

O backend estará disponível em http://localhost:8000

### 2. Setup Bot Telegram

Em outro terminal:

```bash
cd backend

# Ative o ambiente virtual (se não estiver ativo)
source venv/bin/activate

# Configure o token do bot
export BOT_TOKEN="seu_token_aqui"

# Inicie o bot
python bot.py
```

### 3. Setup Frontend

Em outro terminal:

```bash
cd frontend

# Instale as dependências
npm install

# Configure as variáveis de ambiente
# Crie um arquivo .env.local
cat > .env.local << EOF
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_BOT_USERNAME=seu_bot_username
NEXT_PUBLIC_TELEGRAM_APP_ID=seu_app_id
NEXT_PUBLIC_TON_CONNECT_MANIFEST_URL=http://localhost:3000/tonconnect-manifest.json
EOF

# Inicie o servidor de desenvolvimento
npm run dev
```

O frontend estará disponível em http://localhost:3000

## 🔧 Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
# Telegram
BOT_TOKEN=seu_bot_token_aqui
TELEGRAM_API_ID=seu_api_id
TELEGRAM_API_HASH=seu_api_hash
BOT_USERNAME=seu_bot_username

# TON
TON_NETWORK=testnet
TON_ENDPOINT=https://testnet.toncenter.com/api/v2/jsonRPC
TON_API_KEY=sua_chave_api_ton

# Banco de Dados
DATABASE_URL=postgresql://adbounty:password@localhost:5432/adbounty

# Frontend
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_TELEGRAM_APP_ID=seu_app_id
NEXT_PUBLIC_BOT_USERNAME=seu_bot_username
NEXT_PUBLIC_TON_CONNECT_MANIFEST_URL=http://localhost:3000/tonconnect-manifest.json

# Segurança
JWT_SECRET=sua_chave_secreta_jwt

# Ambiente
ENVIRONMENT=development
LOG_LEVEL=INFO
```

## 🧪 Testes

### Backend

```bash
cd backend

# Instale pytest
pip install pytest pytest-cov

# Execute os testes
pytest test_api.py -v

# Com cobertura
pytest test_api.py --cov=. --cov-report=html
```

### Frontend

```bash
cd frontend

# Execute os testes
npm run test

# Com cobertura
npm run test -- --coverage
```

## 📱 Telegram Bot Setup

### 1. Criar um Bot

1. Abra o Telegram e procure por **@BotFather**
2. Envie `/newbot`
3. Siga as instruções para criar um novo bot
4. Copie o token fornecido

### 2. Configurar Webhook (Opcional)

Para produção, configure um webhook em vez de polling:

```bash
curl -X POST https://api.telegram.org/bot<BOT_TOKEN>/setWebhook \
  -H 'Content-Type: application/json' \
  -d '{"url": "https://seu-dominio.com/webhook"}'
```

### 3. Testar o Bot

```bash
# Envie uma mensagem para o bot
# Ou use o comando /start
```

## 🔗 TON Testnet Setup

### 1. Obter Testnet TON

1. Visite https://testnet.toncenter.com
2. Clique em "Get testnet TON"
3. Forneça seu endereço de carteira

### 2. Deploy do Contrato

```bash
cd contracts

# Compile o contrato
func -o escrow.compiled.json escrow.fc

# Deploy (requer tonpy ou similar)
./deploy.sh testnet
```

## 🚢 Deployment

### Vercel (Frontend)

```bash
cd frontend

# Instale Vercel CLI
npm i -g vercel

# Deploy
vercel deploy --prod
```

### Railway (Backend)

```bash
# Instale Railway CLI
npm i -g @railway/cli

# Login
railway login

# Deploy
railway up
```

## 📊 Monitoramento

### Logs do Backend

```bash
# Docker
docker-compose logs -f backend

# Local
# Verifique o console onde o backend está rodando
```

### Logs do Bot

```bash
# Docker
docker-compose logs -f bot

# Local
# Verifique o console onde o bot está rodando
```

### Logs do Frontend

```bash
# Docker
docker-compose logs -f frontend

# Local
# Verifique o console onde o frontend está rodando
```

## 🐛 Troubleshooting

### Erro: "Port 3000 already in use"

```bash
# Mude a porta
npm run dev -- -p 3001
```

### Erro: "Cannot connect to PostgreSQL"

```bash
# Verifique se PostgreSQL está rodando
psql -U postgres

# Crie o banco de dados se necessário
createdb adbounty
```

### Erro: "Bot token is invalid"

```bash
# Verifique o token no .env
# Certifique-se de que está correto
# Não inclua espaços ou caracteres extras
```

### Erro: "TON API key is invalid"

```bash
# Obtenha uma chave em https://toncenter.com
# Adicione ao .env
TON_API_KEY=sua_chave_aqui
```

## 📚 Recursos Úteis

- **Documentação Telegram**: https://core.telegram.org
- **Documentação TON**: https://ton.org/docs
- **FastAPI**: https://fastapi.tiangolo.com
- **Next.js**: https://nextjs.org/docs
- **aiogram**: https://docs.aiogram.dev

## 🆘 Suporte

Se encontrar problemas:

1. Verifique os logs: `docker-compose logs`
2. Consulte a seção Troubleshooting acima
3. Abra uma issue no GitHub
4. Entre em contato: support@adbounty.app

## ✅ Checklist de Setup

- [ ] Node.js 18+ instalado
- [ ] Python 3.11+ instalado
- [ ] Docker instalado (opcional)
- [ ] Repositório clonado
- [ ] Arquivo .env criado
- [ ] Dependências instaladas
- [ ] Banco de dados criado
- [ ] Bot Telegram criado
- [ ] TON testnet funds obtidos
- [ ] Backend iniciado
- [ ] Bot iniciado
- [ ] Frontend iniciado
- [ ] Testes passando
- [ ] Pronto para desenvolvimento!

---

**Próximo passo**: Leia o README.md para entender a arquitetura do projeto.
