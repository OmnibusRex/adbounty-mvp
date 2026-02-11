#!/bin/bash

# AdBounty TON Escrow Contract Deployment Script
# Deploys the escrow contract to TON testnet

set -e

echo "🚀 AdBounty Escrow Contract Deployment"
echo "======================================"

# Configuration
NETWORK=${1:-testnet}
CONTRACT_FILE="escrow.fc"
COMPILED_FILE="escrow.compiled.json"

echo "Network: $NETWORK"
echo "Contract: $CONTRACT_FILE"

# Check if FunC compiler is installed
if ! command -v func &> /dev/null; then
    echo "❌ FunC compiler not found. Installing..."
    # Installation instructions for func compiler
    echo "Please install func compiler from: https://ton.org/docs/#/func"
    exit 1
fi

# Compile FunC contract
echo "📝 Compiling FunC contract..."
func -o $COMPILED_FILE $CONTRACT_FILE

if [ ! -f "$COMPILED_FILE" ]; then
    echo "❌ Compilation failed"
    exit 1
fi

echo "✅ Contract compiled successfully"

# Deploy to testnet
echo "🌐 Deploying to $NETWORK..."

if [ "$NETWORK" = "testnet" ]; then
    ENDPOINT="https://testnet.toncenter.com/api/v2/jsonRPC"
elif [ "$NETWORK" = "mainnet" ]; then
    ENDPOINT="https://toncenter.com/api/v2/jsonRPC"
else
    echo "❌ Unknown network: $NETWORK"
    exit 1
fi

echo "Endpoint: $ENDPOINT"

# Deploy using tonpy or similar tool
# This is a placeholder - actual deployment depends on your toolchain
cat > deploy.py << 'EOF'
import json
import sys
from pathlib import Path

compiled_file = sys.argv[1] if len(sys.argv) > 1 else "escrow.compiled.json"

try:
    with open(compiled_file, 'r') as f:
        contract = json.load(f)
    
    print(f"✅ Contract loaded from {compiled_file}")
    print(f"Code hash: {contract.get('code_hash', 'N/A')}")
    print(f"Data hash: {contract.get('data_hash', 'N/A')}")
    
    # In production, this would deploy to TON using tonpy or similar
    print("\n📋 Deployment steps:")
    print("1. Initialize wallet with TON testnet funds")
    print("2. Deploy contract using tonpy or ton-cli")
    print("3. Save contract address for backend configuration")
    print("4. Update ESCROW_CONTRACT_ADDRESS in .env")
    
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)
EOF

python deploy.py $COMPILED_FILE

# Cleanup
rm -f deploy.py

echo ""
echo "✅ Deployment script completed!"
echo ""
echo "📝 Next steps:"
echo "1. Copy the contract address to .env as ESCROW_CONTRACT_ADDRESS"
echo "2. Test contract on testnet"
echo "3. Update backend with contract address"
echo ""
echo "For more information, visit: https://ton.org/docs/#/func"
