FROM python:3.10-slim

WORKDIR /app

# Primeiro copia apenas o requirements.txt (melhora cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Agora copia TODO o resto do projeto
COPY . .

# Garante que o start.sh está presente e é executável
RUN ls -la start.sh && chmod +x start.sh

CMD ["./start.sh"]
