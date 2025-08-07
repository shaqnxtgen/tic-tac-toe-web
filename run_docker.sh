#!/bin/bash

echo "🐳 Starting Tic Tac Toe with Docker..."

# Build and run with docker-compose
docker-compose up --build -d

echo "✅ Game is running at: http://localhost:8888"
echo ""
echo "🌐 To share with friends, install ngrok:"
echo "   brew install ngrok  # macOS"
echo "   ngrok http 8888"
echo ""
echo "🛑 To stop: docker-compose down"