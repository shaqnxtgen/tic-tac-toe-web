#!/usr/bin/env python3
"""
Quick launcher for the web version of Tic Tac Toe.
"""

import subprocess
import sys
import os

def check_flask():
    """Check if Flask is installed."""
    try:
        import flask
        return True
    except ImportError:
        return False

def install_flask():
    """Install Flask if not present."""
    print("Flask not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Flask>=2.0.0"])
    print("Flask installed successfully!")

def main():
    """Launch the web application."""
    if not check_flask():
        try:
            install_flask()
        except subprocess.CalledProcessError:
            print("Failed to install Flask. Please install manually:")
            print("pip install Flask>=2.0.0")
            sys.exit(1)
    
    print("🚀 Starting Tic Tac Toe Web Server...")
    print("🌐 Open your browser and go to: http://localhost:3000")
    print("⏹️  Press Ctrl+C to stop the server")
    
    try:
        from web_app import app
        app.run(host='localhost', port=3000, debug=True)
    except KeyboardInterrupt:
        print("\n👋 Server stopped. Thanks for playing!")
    except Exception as e:
        print(f"Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()