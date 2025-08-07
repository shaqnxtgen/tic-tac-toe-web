# Developer Notes

## 🧠 AI Algorithm Deep Dive

### Minimax Algorithm Implementation

The Hard AI uses the minimax algorithm, a decision-making algorithm for turn-based games. Here's how it works:

#### Core Concept
- **Maximizing Player**: AI trying to maximize score
- **Minimizing Player**: Human trying to minimize AI's score
- **Recursive Evaluation**: Explores all possible game states

#### Algorithm Steps
1. **Base Case**: If game is over, return score (+1 win, -1 loss, 0 draw)
2. **Maximizing Turn**: Try all moves, return maximum score
3. **Minimizing Turn**: Try all moves, return minimum score
4. **Recursion**: Alternate between maximizing and minimizing

#### Code Walkthrough
```python
def _minimax(self, board: GameBoard, is_maximizing: bool) -> int:
    state = board.get_game_state()
    
    # Terminal states - game is over
    if state == GameState.X_WINS:
        return 1 if self.player == Player.X else -1
    elif state == GameState.O_WINS:
        return 1 if self.player == Player.O else -1
    elif state == GameState.DRAW:
        return 0
    
    if is_maximizing:
        # AI's turn - maximize score
        max_score = float('-inf')
        for row, col in board.get_empty_cells():
            board_copy = board.copy()
            board_copy.board[row][col] = self.player.value
            score = self._minimax(board_copy, False)  # Switch to minimizing
            max_score = max(score, max_score)
        return max_score
    else:
        # Opponent's turn - minimize AI's score
        min_score = float('inf')
        opponent = "O" if self.player == Player.X else "X"
        for row, col in board.get_empty_cells():
            board_copy = board.copy()
            board_copy.board[row][col] = opponent
            score = self._minimax(board_copy, True)  # Switch to maximizing
            min_score = min(score, min_score)
        return min_score
```

#### Why It's Unbeatable
- Evaluates **all possible future game states**
- Always chooses the move that leads to the best outcome
- In Tic Tac Toe, perfect play always results in a draw or win

### Medium AI Strategy

The Medium AI uses a simple but effective strategy hierarchy:

1. **Win Check**: If AI can win in one move, take it
2. **Block Check**: If opponent can win in one move, block it
3. **Center Strategy**: Take center position (1,1) if available
4. **Random Fallback**: Make random move if none of above apply

This creates a challenging opponent without being unbeatable.

## 🏗️ Architecture Decisions

### Why This Structure?

#### Separation of Concerns
- **game_logic.py**: Pure game rules, no UI dependencies
- **ai_player.py**: AI strategies, independent of game display
- **cli_interface.py**: User interaction, no game logic
- **main.py**: Entry point, minimal logic

#### Benefits
- **Testability**: Each module can be tested independently
- **Maintainability**: Changes in one area don't affect others
- **Extensibility**: Easy to add new interfaces (GUI, web, etc.)
- **Reusability**: Game logic can be used in different contexts

### Design Patterns Used

#### Strategy Pattern (AI Difficulties)
```python
class AIPlayer:
    def get_move(self, board):
        if self.difficulty == Difficulty.EASY:
            return self._get_random_move(board)
        elif self.difficulty == Difficulty.MEDIUM:
            return self._get_medium_move(board)
        else:
            return self._get_minimax_move(board)
```

#### State Pattern (Game States)
```python
class GameState(Enum):
    ONGOING = "ongoing"
    X_WINS = "x_wins"
    O_WINS = "o_wins"
    DRAW = "draw"
```

## 🧪 Testing Strategy

### Test Categories

#### Unit Tests
- **Isolated Testing**: Each class tested independently
- **Mock Dependencies**: Use test doubles when needed
- **Edge Cases**: Boundary conditions and error cases

#### Test Structure
```python
class TestGameBoard(unittest.TestCase):
    def setUp(self):
        """Create fresh test fixtures"""
        self.board = GameBoard()
    
    def test_specific_behavior(self):
        """Test one specific behavior"""
        # Arrange
        # Act
        # Assert
```

### Running Tests

#### Basic Test Execution
```bash
# Run all tests
python -m unittest discover tests/

# Run specific test class
python -m unittest tests.test_game_logic.TestGameBoard

# Run specific test method
python -m unittest tests.test_game_logic.TestGameBoard.test_initial_state
```

#### Advanced Testing
```bash
# Run with coverage (requires coverage.py)
pip install coverage
coverage run -m unittest discover tests/
coverage report
coverage html  # Creates htmlcov/ directory

# Run with pytest (alternative test runner)
pip install pytest
pytest tests/ -v
```

### Writing New Tests

#### Test Naming Convention
- `test_<functionality>_<condition>_<expected_result>`
- Example: `test_make_move_valid_position_returns_true`

#### Test Structure Template
```python
def test_new_feature(self):
    """Test description of what this test verifies."""
    # Arrange - Set up test data
    board = GameBoard()
    
    # Act - Perform the action being tested
    result = board.make_move(0, 0)
    
    # Assert - Verify the expected outcome
    self.assertTrue(result)
    self.assertEqual(board.board[0][0], "X")
```

## 🚀 Adding New Features

### Adding a New AI Difficulty

1. **Extend Difficulty Enum**:
```python
class Difficulty(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"
    EXPERT = "expert"  # New difficulty
```

2. **Implement Strategy**:
```python
def get_move(self, board: GameBoard) -> Tuple[int, int]:
    if self.difficulty == Difficulty.EXPERT:
        return self._get_expert_move(board)
    # ... existing code
```

3. **Add Strategy Method**:
```python
def _get_expert_move(self, board: GameBoard) -> Tuple[int, int]:
    """Implement expert-level strategy."""
    # Your advanced AI logic here
    pass
```

4. **Update CLI Interface**:
```python
def get_difficulty(self) -> Difficulty:
    print("4. Expert (Advanced strategy)")
    # Handle choice "4"
```

### Adding GUI Interface

1. **Create New Interface Module**:
```python
# gui_interface.py
import tkinter as tk
from game_logic import GameBoard, GameState
from ai_player import AIPlayer

class GUIInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.board = GameBoard()
        self.setup_ui()
    
    def setup_ui(self):
        """Create the GUI elements."""
        # Implementation here
```

2. **Update Main Entry Point**:
```python
# main.py
parser.add_argument('--gui', action='store_true', 
                   help='Launch GUI interface')

if args.gui:
    from gui_interface import GUIInterface
    game = GUIInterface()
    game.run()
else:
    from cli_interface import CLIInterface
    game = CLIInterface()
    game.run_game()
```

### Adding Game Statistics

1. **Extend GameBoard**:
```python
class GameBoard:
    def __init__(self):
        # ... existing code
        self.stats = {
            'games_played': 0,
            'x_wins': 0,
            'o_wins': 0,
            'draws': 0
        }
    
    def update_stats(self, result: GameState):
        """Update game statistics."""
        self.stats['games_played'] += 1
        if result == GameState.X_WINS:
            self.stats['x_wins'] += 1
        # ... etc
```

2. **Display in Interface**:
```python
def display_stats(self):
    """Show game statistics."""
    stats = self.board.stats
    print(f"Games Played: {stats['games_played']}")
    # ... etc
```

## 🔧 Performance Optimization

### Minimax Optimizations

#### Alpha-Beta Pruning
```python
def _minimax_alpha_beta(self, board, depth, alpha, beta, is_maximizing):
    """Optimized minimax with alpha-beta pruning."""
    # Base case
    if depth == 0 or game_over:
        return evaluate(board)
    
    if is_maximizing:
        max_eval = float('-inf')
        for move in get_moves(board):
            eval_score = self._minimax_alpha_beta(
                make_move(board, move), depth-1, alpha, beta, False)
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break  # Beta cutoff
        return max_eval
    # ... minimizing case
```

#### Transposition Table
```python
class AIPlayer:
    def __init__(self, difficulty, player):
        # ... existing code
        self.transposition_table = {}  # Cache for board positions
    
    def _minimax_with_cache(self, board, is_maximizing):
        board_key = self._board_to_key(board)
        if board_key in self.transposition_table:
            return self.transposition_table[board_key]
        
        score = self._minimax(board, is_maximizing)
        self.transposition_table[board_key] = score
        return score
```

### Memory Optimization

#### Board Representation
```python
# Instead of 2D list, use single integer with bit manipulation
class OptimizedBoard:
    def __init__(self):
        self.x_positions = 0  # 9-bit integer
        self.o_positions = 0  # 9-bit integer
    
    def set_position(self, pos, player):
        if player == 'X':
            self.x_positions |= (1 << pos)
        else:
            self.o_positions |= (1 << pos)
```

## 🐛 Debugging Tips

### Common Issues

#### Import Errors
```python
# Problem: ModuleNotFoundError
# Solution: Add parent directory to path
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
```

#### AI Taking Too Long
```python
# Problem: Minimax is slow on larger boards
# Solution: Add depth limiting
def _minimax(self, board, is_maximizing, depth=0, max_depth=9):
    if depth >= max_depth:
        return self._evaluate_position(board)
    # ... rest of minimax
```

### Debugging Tools

#### Print Board State
```python
def debug_print_board(self):
    """Print board state for debugging."""
    print("Current board:")
    for i, row in enumerate(self.board):
        print(f"Row {i}: {row}")
    print(f"Current player: {self.current_player}")
    print(f"Game state: {self.get_game_state()}")
```

#### Log AI Decisions
```python
def get_move(self, board):
    move = self._calculate_move(board)
    print(f"AI ({self.difficulty.value}) chose: {move}")
    return move
```

## 📈 Future Enhancements

### Potential Features
- **Network Play**: Multiplayer over internet
- **Tournament Mode**: Multiple games with scoring
- **Custom Board Sizes**: 4x4, 5x5 variants
- **AI vs AI**: Watch different strategies compete
- **Move History**: Undo/redo functionality
- **Themes**: Different visual styles
- **Sound Effects**: Audio feedback
- **Animations**: Smooth move transitions

### Advanced AI Features
- **Opening Book**: Predefined optimal opening moves
- **Endgame Database**: Perfect play in endgame positions
- **Learning AI**: Neural network that improves over time
- **Personality**: Different AI "personalities" with playing styles

This should give you a comprehensive understanding of the codebase and how to extend it! 🚀