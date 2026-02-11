# AdBounty - Deployment Guide

Guia completo para fazer deploy do AdBounty em produção.

## 🎯 Arquitetura de Deployment

```
┌─────────────────────────────────────────────────────────┐
│                    Usuários Finais                      │
└────────────────┬────────────────────────────────────────┘
                 │
        ┌────────┴────────┐
        │                 │
    ┌───▼────┐      ┌────▼────┐
    │ Vercel │      │ Telegram │
    │Frontend│      │   Bot    │
    └───┬────┘      └────┬─────┘
        │                │
        └────────┬───────┘
                 │
         ┌───────▼────────┐
         │  Railway API   │
         │   (Backend)    │
         └───────┬────────┘
                 │
        ┌────────┴────────┐
        │                 │
    ┌───▼────┐      ┌────▼────┐
    │PostgreSQL    │ TON Node │
    │(Railway)    │(Testnet) │
    └──────────    └──────────┘
```

## 📦 Componentes

### Frontend (Vercel)
- Next.js 14 application
- Static + dynamic rendering
- Edge functions para API calls
- CDN global

### Backend (Railway)
- FastAPI application
- Python 3.11 runtime
- PostgreSQL database
- Redis cache (opcional)

### Bot (Railway)
- aiogram bot service
- Rodando como worker
- Acesso ao backend

### Smart Contract (TON Testnet)
- FunC contract compilado
- Deployed em testnet
- Endereço fixo no .env

## 🚀 Deployment Passo a Passo

### 1. Preparação Inicial

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/adbounty.git
cd adbounty

# Crie um repositório privado no GitHub
git remote set-url origin https://github.com/seu-usuario/adbounty.git
git push -u origin main
```

### 2. Deploy Frontend (Vercel)

#### 2.1 Setup Vercel

```bash
# Instale Vercel CLI
npm i -g vercel

# Faça login
vercel login

# Configure o projeto
cd frontend
vercel link
```

#### 2.2 Configurar Variáveis de Ambiente

No dashboard do Vercel, adicione:

```
NEXT_PUBLIC_API_URL=https://adbounty-api.railway.app
NEXT_PUBLIC_BOT_USERNAME=seu_bot_username
NEXT_PUBLIC_TELEGRAM_APP_ID=seu_telegram_app_id
NEXT_PUBLIC_TON_CONNECT_MANIFEST_URL=https://adbounty.vercel.app/tonconnect-manifest.json
JWT_SECRET=sua_chave_secreta_jwt
```

#### 2.3 Deploy

```bash
# Deploy para produção
vercel deploy --prod

# Ou use GitHub Actions (recomendado)
git push origin main
```

**URL**: https://adbounty.vercel.app

### 3. Deploy Backend (Railway)

#### 3.1 Setup Railway

1. Visite https://railway.app
2. Clique em "New Project"
3. Selecione "Deploy from GitHub"
4. Conecte seu repositório GitHub

#### 3.2 Configurar Variáveis de Ambiente

No dashboard do Railway, adicione:

```
DATABASE_URL=postgresql://user:pass@host:5432/adbounty
BOT_TOKEN=seu_bot_token
TELEGRAM_API_ID=seu_api_id
TELEGRAM_API_HASH=seu_api_hash
TON_NETWORK=testnet
TON_ENDPOINT=https://testnet.toncenter.com/api/v2/jsonRPC
TON_API_KEY=sua_chave_api_ton
ESCROW_CONTRACT_ADDRESS=seu_contrato_address
ENVIRONMENT=production
LOG_LEVEL=INFO
JWT_SECRET=sua_chave_secreta_jwt
```

#### 3.3 Configurar Build & Deploy

No Railway:
1. Selecione "Services"
2. Clique em "New Service"
3. Selecione "GitHub Repo"
4. Configure:
   - Root directory: `./backend`
   - Build command: `pip install -r requirements.txt`
   - Start command: `python -m uvicorn main:app --host 0.0.0.0 --port $PORT`

#### 3.4 Deploy

```bash
# Ou via CLI
railway up
```

**URL**: https://adbounty-api.railway.app

### 4. Deploy Bot (Railway Worker)

#### 4.1 Criar Worker Service

No Railway:
1. Clique em "New Service"
2. Selecione "GitHub Repo"
3. Configure:
   - Root directory: `./backend`
   - Build command: `pip install -r requirements.txt`
   - Start command: `python bot.py`

#### 4.2 Configurar Variáveis

Use as mesmas variáveis do backend, adicione:

```
BACKEND_URL=https://adbounty-api.railway.app
```

### 5. Deploy Smart Contract (TON)

#### 5.1 Compilar Contrato

```bash
cd contracts

# Instale o compilador FunC
# https://ton.org/docs/#/func

# Compile
func -o escrow.compiled.json escrow.fc
```

#### 5.2 Deploy no Testnet

```bash
# Use tonpy ou ton-cli
python deploy.py escrow.compiled.json

# Ou use o script
./deploy.sh testnet
```

#### 5.3 Salvar Endereço

Após o deploy, salve o endereço do contrato:

```bash
# Adicione ao Railway como variável de ambiente
ESCROW_CONTRACT_ADDRESS=EQDk2ImpM...
```

### 6. Configurar Domínio Customizado

#### Vercel Frontend

1. Vá para Project Settings
2. Clique em "Domains"
3. Adicione seu domínio (ex: adbounty.app)
4. Configure DNS records

#### Railway Backend

1. Vá para Project Settings
2. Clique em "Custom Domain"
3. Adicione seu domínio (ex: api.adbounty.app)
4. Configure DNS records

### 7. Setup CI/CD (GitHub Actions)

O arquivo `.github/workflows/deploy.yml` já está configurado. Ele:

1. Executa testes no push
2. Faz build dos componentes
3. Faz deploy automático para Vercel e Railway

Para ativar:

```bash
# Adicione secrets no GitHub
# Settings → Secrets and variables → Actions

# Secrets necessários:
VERCEL_TOKEN
VERCEL_ORG_ID
VERCEL_PROJECT_ID
RAILWAY_TOKEN
```

## 📊 Monitoramento

### Vercel Analytics

1. Dashboard do Vercel
2. Abra seu projeto
3. Vá para "Analytics"
4. Monitore performance, uptime, etc.

### Railway Monitoring

1. Dashboard do Railway
2. Abra seu projeto
3. Vá para "Monitoring"
4. Monitore CPU, memória, logs

### Logs

```bash
# Vercel
vercel logs

# Railway
railway logs

# Backend
curl https://adbounty-api.railway.app/health
```

## 🔐 Segurança

### HTTPS

Ambas Vercel e Railway fornecem HTTPS automático.

### Variáveis de Ambiente

Nunca commite `.env` ou secrets. Use:

```bash
# Vercel
vercel env add SECRET_KEY

# Railway
# Use o dashboard
```

### CORS

Configure CORS no backend:

```python
# backend/main.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://adbounty.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Rate Limiting

Implemente rate limiting:

```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

@app.get("/api/endpoint")
@limiter.limit("100/minute")
async def endpoint(request: Request):
    pass
```

## 🚨 Troubleshooting

### Erro 502 Bad Gateway

```bash
# Verifique se o backend está rodando
curl https://adbounty-api.railway.app/health

# Verifique os logs
railway logs

# Reinicie o serviço
railway restart
```

### Erro de Conexão com Banco de Dados

```bash
# Verifique a string de conexão
echo $DATABASE_URL

# Teste a conexão
psql $DATABASE_URL

# Verifique se o banco existe
psql -l
```

### Bot não responde

```bash
# Verifique se o bot está rodando
railway logs -s bot

# Verifique o token
echo $BOT_TOKEN

# Teste o bot
curl -X POST https://api.telegram.org/bot$BOT_TOKEN/getMe
```

### Contrato não funciona

```bash
# Verifique o endereço
echo $ESCROW_CONTRACT_ADDRESS

# Teste o contrato
curl https://testnet.toncenter.com/api/v2/jsonRPC \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"getAddressState","params":{"address":"'$ESCROW_CONTRACT_ADDRESS'"},"id":1}'
```

## 📈 Performance

### Frontend Optimization

- [ ] Ativar Vercel Analytics
- [ ] Usar Image Optimization
- [ ] Implementar Code Splitting
- [ ] Cache estático

### Backend Optimization

- [ ] Ativar Redis cache
- [ ] Implementar database indexing
- [ ] Usar connection pooling
- [ ] Implementar rate limiting

## 🔄 Rollback

Se algo der errado:

### Vercel

```bash
# Veja deployments anteriores
vercel list

# Rollback para versão anterior
vercel rollback
```

### Railway

```bash
# Veja deployments anteriores
railway deployment list

# Rollback para versão anterior
railway deployment rollback <id>
```

## 📝 Checklist de Deployment

- [ ] Todas as variáveis de ambiente configuradas
- [ ] Testes passando
- [ ] Build local funcionando
- [ ] Domínio customizado configurado
- [ ] HTTPS ativado
- [ ] Monitoramento configurado
- [ ] Backups configurados
- [ ] Logs centralizados
- [ ] Rate limiting ativado
- [ ] CORS configurado
- [ ] Secrets seguros
- [ ] CI/CD funcionando
- [ ] Documentação atualizada

## 🎉 Deployment Completo!

Seu AdBounty está pronto para produção!

- Frontend: https://adbounty.vercel.app
- Backend: https://adbounty-api.railway.app
- Bot: @seu_bot_username

---

**Próximos passos**: Monitore a aplicação, colete feedback dos usuários e itere.
