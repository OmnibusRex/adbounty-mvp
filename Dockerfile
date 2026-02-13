FROM python:3.10-slim

WORKDIR /app

# Copia requirements primeiro (melhora cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# COPIA TODOS OS ARQUIVOS (incluindo start.sh)
COPY . .

# Garante que start.sh é executável
RUN chmod +x start.sh

# Verifica se o arquivo está lá (debug)
RUN ls -la start.sh

CMD ["./start.sh"]
