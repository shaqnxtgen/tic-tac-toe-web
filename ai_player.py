"""
AI player implementation with three difficulty levels.

This module contains the AIPlayer class that implements different strategies
for the computer opponent: Easy (random), Medium (basic strategy), and Hard (minimax).
"""

import random
from typing import Tuple, Optional
from enum import Enum
from game_logic import GameBoard, Player, GameState


class Difficulty(Enum):
    """AI difficulty levels."""
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class AIPlayer:
    """
    AI player that can play at different difficulty levels.
    
    Attributes:
        difficulty: The AI difficulty level
        player: The player symbol (X or O) this AI represents
    """
    
    def __init__(self, difficulty: Difficulty, player: Player):
        """
        Initialize AI player.
        
        Args:
            difficulty: AI difficulty level
            player: Player symbol (X or O)
        """
        self.difficulty = difficulty
        self.player = player
    
    def get_move(self, board: GameBoard) -> Tuple[int, int]:
        """
        Get the AI's next move based on difficulty level.
        
        Args:
            board: Current game board state
            
        Returns:
            Tuple of (row, col) for the AI's move
        """
        if self.difficulty == Difficulty.EASY:
            return self._get_random_move(board)
        elif self.difficulty == Difficulty.MEDIUM:
            return self._get_medium_move(board)
        else:  # HARD
            return self._get_minimax_move(board)
    
    def _get_random_move(self, board: GameBoard) -> Tuple[int, int]:
        """Get a random valid move."""
        empty_cells = board.get_empty_cells()
        return random.choice(empty_cells)
    
    def _get_medium_move(self, board: GameBoard) -> Tuple[int, int]:
        """
        Get move using basic strategy:
        1. Win if possible
        2. Block opponent win
        3. Take center if available
        4. Random move
        """
        # Try to win
        win_move = self._find_winning_move(board, self.player.value)
        if win_move:
            return win_move
        
        # Block opponent win
        opponent = "O" if self.player == Player.X else "X"
        block_move = self._find_winning_move(board, opponent)
        if block_move:
            return block_move
        
        # Take center if available
        if board.is_valid_move(1, 1):
            return (1, 1)
        
        # Random move
        return self._get_random_move(board)
    
    def _get_minimax_move(self, board: GameBoard) -> Tuple[int, int]:
        """Get optimal move using minimax algorithm."""
        best_score = float('-inf')
        best_move = None
        
        for row, col in board.get_empty_cells():
            # Make temporary move
            board_copy = board.copy()
            board_copy.board[row][col] = self.player.value
            
            # Get minimax score
            score = self._minimax(board_copy, False)
            
            if score > best_score:
                best_score = score
                best_move = (row, col)
        
        return best_move
    
    def _minimax(self, board: GameBoard, is_maximizing: bool) -> int:
        """
        Minimax algorithm implementation.
        
        Args:
            board: Current board state
            is_maximizing: True if maximizing player's turn
            
        Returns:
            Score for this board state
        """
        state = board.get_game_state()
        
        # Terminal states
        if state == GameState.X_WINS:
            return 1 if self.player == Player.X else -1
        elif state == GameState.O_WINS:
            return 1 if self.player == Player.O else -1
        elif state == GameState.DRAW:
            return 0
        
        if is_maximizing:
            max_score = float('-inf')
            for row, col in board.get_empty_cells():
                board_copy = board.copy()
                board_copy.board[row][col] = self.player.value
                score = self._minimax(board_copy, False)
                max_score = max(score, max_score)
            return max_score
        else:
            min_score = float('inf')
            opponent = "O" if self.player == Player.X else "X"
            for row, col in board.get_empty_cells():
                board_copy = board.copy()
                board_copy.board[row][col] = opponent
                score = self._minimax(board_copy, True)
                min_score = min(score, min_score)
            return min_score
    
    def _find_winning_move(self, board: GameBoard, player_symbol: str) -> Optional[Tuple[int, int]]:
        """
        Find a move that would result in a win for the given player.
        
        Args:
            board: Current board state
            player_symbol: Player symbol to check for winning moves
            
        Returns:
            Winning move coordinates or None if no winning move exists
        """
        for row, col in board.get_empty_cells():
            # Try the move
            board_copy = board.copy()
            board_copy.board[row][col] = player_symbol
            
            # Check if it's a winning move
            state = board_copy.get_game_state()
            if ((player_symbol == "X" and state == GameState.X_WINS) or
                (player_symbol == "O" and state == GameState.O_WINS)):
                return (row, col)
        
        return None