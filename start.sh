#!/bin/bash
echo "=== Iniciando AdBounty MVP ==="

# Instala serve globalmente se necessário
npm install -g serve

# Inicia o servidor de arquivos estáticos na porta 3000 (para o Mini App)
serve -s public -l 3000 &
echo "✅ Mini App rodando na porta 3000"

# Inicia o backend FastAPI na porta $PORT (definida pelo Railway)
uvicorn backend.main:app --host 0.0.0.0 --port $PORT &
echo "✅ Backend rodando na porta $PORT"

# Inicia o bot
python backend/bot_simple.py
