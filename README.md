# Tic Tac Toe - Python Edition

A well-structured, feature-rich Tic Tac Toe game implemented in Python with clean architecture, multiple difficulty levels, and an engaging CLI interface.

## 🎮 Features

- **Multiple Game Modes**: Human vs Human, Human vs AI
- **3 AI Difficulty Levels**:
  - **Easy**: Random moves
  - **Medium**: Basic strategy (win/block/center)
  - **Hard**: Unbeatable minimax algorithm
- **Colorful CLI Interface**: Enhanced user experience with ANSI colors
- **Clean Architecture**: Modular design with separated concerns
- **Comprehensive Testing**: Unit tests for all core functionality
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Flask (auto-installed by web launcher)

### Installation & Running

1. **Clone or download the project**:
   ```bash
   # If using git
   git clone <repository-url>
   cd tic_tac_toe
   
   # Or simply download and extract the files
   ```

2. **Run the CLI game**:
   ```bash
   python3 main.py
   ```

3. **Run the Web game**:
   ```bash
   python3 run_web.py
   # Then open http://localhost:3000 in your browser
   ```

3. **Run tests**:
   ```bash
   python -m pytest tests/
   # or
   python -m unittest discover tests/
   ```

## 🎯 How to Play

1. **Start the game**: Run `python main.py`
2. **Choose game mode**: Human vs AI or Human vs Human
3. **Select difficulty** (if playing vs AI): Easy, Medium, or Hard
4. **Make moves**: Enter coordinates as `row,col` (e.g., `1,2`) or `row col` (e.g., `1 2`)
5. **Win conditions**: Get 3 in a row (horizontally, vertically, or diagonally)

### Game Controls
- **Move format**: `row,col` or `row col` (coordinates from 0-2)
- **Example moves**: `0,0` (top-left), `1,1` (center), `2,2` (bottom-right)
- **Quit anytime**: Press `Ctrl+C`

## 📁 Project Structure

```
tic_tac_toe/
├── main.py              # Entry point and CLI argument handling
├── game_logic.py        # Core game rules and board management
├── ai_player.py         # AI implementation with 3 difficulty levels
├── cli_interface.py     # Text-based user interface with colors
├── requirements.txt     # Project dependencies (none for core)
├── README.md           # This file
└── tests/              # Unit tests
    ├── __init__.py
    ├── test_game_logic.py
    └── test_ai_player.py
```

## 🏗️ Architecture Overview

### Core Components

1. **GameBoard** (`game_logic.py`):
   - Manages 3x3 game board state
   - Validates moves and checks win conditions
   - Handles player turns and game state

2. **AIPlayer** (`ai_player.py`):
   - Implements three difficulty levels
   - Uses minimax algorithm for hard difficulty
   - Provides strategic play for medium difficulty

3. **CLIInterface** (`cli_interface.py`):
   - Handles user interaction and display
   - Provides colorful, engaging interface
   - Manages game flow and input validation

4. **Main** (`main.py`):
   - Entry point with argument parsing
   - Error handling and graceful shutdown

### Design Principles

- **Separation of Concerns**: Each module has a single responsibility
- **Clean Code**: PEP8 compliant with comprehensive docstrings
- **Testability**: All core logic is unit tested
- **Extensibility**: Easy to add new features or AI strategies

## 🧪 Testing

The project includes comprehensive unit tests covering:

- **Game Logic**: Board state, moves, win conditions
- **AI Behavior**: All difficulty levels and strategies
- **Edge Cases**: Invalid moves, boundary conditions

### Running Tests

```bash
# Run all tests
python -m unittest discover tests/

# Run specific test file
python -m unittest tests.test_game_logic

# Run with verbose output
python -m unittest discover tests/ -v
```

## 🔧 Development Guide

### Adding New Features

1. **New AI Strategy**:
   ```python
   # In ai_player.py, add new difficulty level
   class Difficulty(Enum):
       EXPERT = "expert"  # Add new level
   
   # Implement strategy in AIPlayer.get_move()
   elif self.difficulty == Difficulty.EXPERT:
       return self._get_expert_move(board)
   ```

2. **New Game Mode**:
   ```python
   # In cli_interface.py, extend get_game_mode()
   print("3. Tournament Mode")
   # Add handling logic
   ```

3. **GUI Interface**:
   ```python
   # Create new file: gui_interface.py
   import tkinter as tk
   from game_logic import GameBoard
   # Implement TkinterInterface class
   ```

### Code Style Guidelines

- Follow PEP8 conventions
- Use type hints for function parameters and returns
- Write docstrings for all classes and methods
- Keep functions focused and small
- Use meaningful variable names

### AI Algorithm Details

#### Easy AI (Random)
- Selects random valid moves
- No strategy involved
- Good for beginners

#### Medium AI (Basic Strategy)
1. **Win**: Take winning move if available
2. **Block**: Block opponent's winning move
3. **Center**: Take center position if free
4. **Random**: Make random move otherwise

#### Hard AI (Minimax)
- Uses minimax algorithm with perfect play
- Evaluates all possible game states
- Guarantees optimal moves (never loses)
- Recursively scores positions:
  - Win: +1, Loss: -1, Draw: 0

## 📦 Packaging & Distribution

### Option 1: PyInstaller (Standalone Executable)

```bash
# Install PyInstaller
pip install pyinstaller

# Create executable
pyinstaller --onefile --name tic-tac-toe main.py

# Executable will be in dist/ folder
```

### Option 2: Python Package

```bash
# Create setup.py
cat > setup.py << EOF
from setuptools import setup, find_packages

setup(
    name="tic-tac-toe-game",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'tic-tac-toe=main:main',
        ],
    },
    python_requires='>=3.7',
)
EOF

# Install locally
pip install -e .

# Build distribution
python setup.py sdist bdist_wheel
```

### Option 3: Docker Container

```bash
# Create Dockerfile
cat > Dockerfile << EOF
FROM python:3.9-slim
WORKDIR /app
COPY . .
CMD ["python", "main.py"]
EOF

# Build and run
docker build -t tic-tac-toe .
docker run -it tic-tac-toe
```

## 🌐 Sharing Your Game

### GitHub Repository
1. Create repository on GitHub
2. Push your code
3. Add installation instructions in README
4. Tag releases for versions

### Python Package Index (PyPI)
```bash
# Upload to PyPI (requires account)
pip install twine
twine upload dist/*
```

### Share Executable
- Use PyInstaller to create standalone executable
- Share the single file - no Python installation required
- Works on same OS type (Windows .exe, macOS app, Linux binary)

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Make changes and add tests
4. Ensure all tests pass: `python -m unittest discover tests/`
5. Submit pull request

## 📝 License

This project is open source and available under the MIT License.

## 🎉 Enjoy Playing!

Have fun playing Tic Tac Toe! Try to beat the Hard AI - it's unbeatable, but you might manage a draw! 🎯