.PHONY: help install dev test build deploy clean

help:
	@echo "AdBounty - Makefile Commands"
	@echo "============================"
	@echo ""
	@echo "Development:"
	@echo "  make install       - Install all dependencies"
	@echo "  make dev           - Start development environment (Docker)"
	@echo "  make dev-local     - Start development locally"
	@echo ""
	@echo "Testing:"
	@echo "  make test          - Run all tests"
	@echo "  make test-backend  - Run backend tests"
	@echo "  make test-frontend - Run frontend tests"
	@echo ""
	@echo "Building:"
	@echo "  make build         - Build all components"
	@echo "  make build-backend - Build backend Docker image"
	@echo "  make build-frontend - Build frontend"
	@echo ""
	@echo "Deployment:"
	@echo "  make deploy-frontend - Deploy frontend to Vercel"
	@echo "  make deploy-backend  - Deploy backend to Railway"
	@echo "  make deploy-contract - Deploy contract to TON testnet"
	@echo ""
	@echo "Maintenance:"
	@echo "  make clean         - Clean build artifacts"
	@echo "  make lint          - Run linters"
	@echo "  make format        - Format code"

install:
	@echo "Installing dependencies..."
	cd backend && pip install -r requirements.txt
	cd frontend && npm install
	@echo "✅ Dependencies installed"

dev:
	@echo "Starting development environment with Docker..."
	docker-compose up -d
	@echo "✅ Development environment started"
	@echo "Frontend: http://localhost:3000"
	@echo "Backend: http://localhost:8000"
	@echo "API Docs: http://localhost:8000/docs"

dev-local:
	@echo "Starting development environment locally..."
	@echo "Make sure PostgreSQL and Redis are running"
	@echo ""
	@echo "Starting backend..."
	cd backend && python main.py &
	@echo ""
	@echo "Starting bot..."
	cd backend && python bot.py &
	@echo ""
	@echo "Starting frontend..."
	cd frontend && npm run dev &
	@echo ""
	@echo "✅ All services started"

test:
	@echo "Running all tests..."
	make test-backend
	make test-frontend

test-backend:
	@echo "Running backend tests..."
	cd backend && pytest test_api.py -v

test-frontend:
	@echo "Running frontend tests..."
	cd frontend && npm run test

build:
	@echo "Building all components..."
	make build-backend
	make build-frontend

build-backend:
	@echo "Building backend Docker image..."
	docker build -f backend/Dockerfile -t adbounty-backend:latest .
	@echo "✅ Backend image built"

build-frontend:
	@echo "Building frontend..."
	cd frontend && npm run build
	@echo "✅ Frontend built"

deploy-frontend:
	@echo "Deploying frontend to Vercel..."
	cd frontend && vercel deploy --prod
	@echo "✅ Frontend deployed"

deploy-backend:
	@echo "Deploying backend to Railway..."
	railway up
	@echo "✅ Backend deployed"

deploy-contract:
	@echo "Deploying contract to TON testnet..."
	cd contracts && ./deploy.sh testnet
	@echo "✅ Contract deployed"

clean:
	@echo "Cleaning build artifacts..."
	rm -rf backend/__pycache__ backend/*.pyc
	rm -rf frontend/.next frontend/out frontend/node_modules
	rm -rf dist build *.egg-info
	@echo "✅ Cleaned"

lint:
	@echo "Running linters..."
	cd backend && pylint backend/*.py
	cd frontend && npm run lint

format:
	@echo "Formatting code..."
	cd backend && black backend/
	cd frontend && prettier --write .
	@echo "✅ Code formatted"

stop:
	@echo "Stopping development environment..."
	docker-compose down
	@echo "✅ Stopped"

logs:
	@echo "Showing logs..."
	docker-compose logs -f

ps:
	@echo "Running containers..."
	docker-compose ps
# Inicia o banco de dados e sincroniza o schema
db-push:
	pnpm drizzle-kit push

# Inicia o projeto completo (Server + Metro)
dev:
	npm run dev

# Abre o túnel do ngrok na porta do servidor
tunnel:
	ngrok http 3000

# Atalho para limpar o banco caso queira começar do zero
db-reset:
	rm sqlite.db && pnpm drizzle-kit push

# Comando "mestre" para ver o banco visualmente
studio:
	npx drizzle-kit studio
