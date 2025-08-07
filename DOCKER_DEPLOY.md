# Docker Deployment Guide

## 🐳 Run with Docker Compose

### Prerequisites
- Docker Desktop installed
- ngrok (for sharing with friends)

### Quick Start
```bash
cd ~/Documents/tic_tac_toe

# Run the game
./run_docker.sh

# Game runs at: http://localhost:3000
```

### Manual Commands
```bash
# Build and run
docker-compose up --build -d

# Stop
docker-compose down

# View logs
docker-compose logs -f
```

## 🌐 Share with Friends

### Option 1: ngrok (Recommended)
```bash
# Install ngrok
brew install ngrok  # macOS
# or download from https://ngrok.com

# Create tunnel
ngrok http 3000

# Share the https URL with friends!
```

### Option 2: Tailscale (Private Network)
```bash
# Install Tailscale on your machine and friends' devices
# Share your Tailscale IP: http://100.x.x.x:3000
```

### Option 3: Local Network
```bash
# Find your local IP
ifconfig | grep "inet " | grep -v 127.0.0.1

# Share: http://YOUR_LOCAL_IP:3000
# (Only works if friends are on same WiFi)
```

## 🎮 Features
- Runs in isolated container
- Auto-restarts if crashes
- Easy to stop/start
- Same great game with AI opponents!