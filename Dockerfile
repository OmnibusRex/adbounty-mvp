FROM python:3.10-slim

WORKDIR /app

# Instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código
COPY . .

# Torna o script executável
RUN chmod +x start.sh

# Expõe a porta
EXPOSE 8000

# Comando para iniciar
CMD ["./start.sh"]
