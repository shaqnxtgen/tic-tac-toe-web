# Deployment Guide

## 🚀 Quick Deploy Options

### Option 1: Heroku (Free/Easy)

1. **Create Heroku account**: https://heroku.com
2. **Install Heroku CLI**: https://devcenter.heroku.com/articles/heroku-cli
3. **Deploy**:
```bash
cd ~/Documents/tic_tac_toe
git init
git add .
git commit -m "Initial commit"
heroku create your-tictactoe-app
git push heroku main
```

### Option 2: Railway (Free/Easy)

1. **Create Railway account**: https://railway.app
2. **Connect GitHub repo**
3. **Deploy automatically** - Railway detects Flask apps

### Option 3: Render (Free)

1. **Create Render account**: https://render.com
2. **Connect GitHub repo**
3. **Create Web Service** with these settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`

## 📋 GitHub Setup

```bash
cd ~/Documents/tic_tac_toe

# Initialize git
git init
git add .
git commit -m "Initial commit: Tic Tac Toe web game"

# Create GitHub repo (replace YOUR_USERNAME)
gh repo create tic-tac-toe-web --public
git remote add origin https://github.com/YOUR_USERNAME/tic-tac-toe-web.git
git push -u origin main
```

## 🌐 Share Your Game

After deployment, you'll get a URL like:
- Heroku: `https://your-tictactoe-app.herokuapp.com`
- Railway: `https://your-app.railway.app`
- Render: `https://your-app.onrender.com`

Share this URL with friends to play online! 🎮