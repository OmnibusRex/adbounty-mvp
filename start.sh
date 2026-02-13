#!/bin/bash
echo "Iniciando backend..."
uvicorn backend.main:app --host 0.0.0.0 --port $PORT &
echo "Iniciando bot..."
python backend/bot_simple.py
