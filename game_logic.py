"""
Core game logic for Tic Tac Toe.

This module contains the GameBoard class that manages the game state,
validates moves, and checks for win conditions.
"""

from typing import List, Optional, Tuple
from enum import Enum


class Player(Enum):
    """Enum representing the two players."""
    X = "X"
    O = "O"


class GameState(Enum):
    """Enum representing the current state of the game."""
    ONGOING = "ongoing"
    X_WINS = "x_wins"
    O_WINS = "o_wins"
    DRAW = "draw"


class GameBoard:
    """
    Manages the Tic Tac Toe game board and game state.
    
    Attributes:
        board: 3x3 grid representing the game board
        current_player: The player whose turn it is
    """
    
    def __init__(self):
        """Initialize an empty 3x3 game board."""
        self.board: List[List[Optional[str]]] = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = Player.X
    
    def make_move(self, row: int, col: int) -> bool:
        """
        Make a move on the board.
        
        Args:
            row: Row index (0-2)
            col: Column index (0-2)
            
        Returns:
            True if move was successful, False if invalid
        """
        if not self.is_valid_move(row, col):
            return False
        
        self.board[row][col] = self.current_player.value
        self.current_player = Player.O if self.current_player == Player.X else Player.X
        return True
    
    def is_valid_move(self, row: int, col: int) -> bool:
        """Check if a move is valid."""
        return (0 <= row < 3 and 0 <= col < 3 and 
                self.board[row][col] is None)
    
    def get_game_state(self) -> GameState:
        """
        Check the current game state.
        
        Returns:
            GameState enum indicating current state
        """
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] is not None:
                return GameState.X_WINS if row[0] == "X" else GameState.O_WINS
        
        # Check columns
        for col in range(3):
            if (self.board[0][col] == self.board[1][col] == self.board[2][col] 
                and self.board[0][col] is not None):
                return GameState.X_WINS if self.board[0][col] == "X" else GameState.O_WINS
        
        # Check diagonals
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] 
            and self.board[0][0] is not None):
            return GameState.X_WINS if self.board[0][0] == "X" else GameState.O_WINS
        
        if (self.board[0][2] == self.board[1][1] == self.board[2][0] 
            and self.board[0][2] is not None):
            return GameState.X_WINS if self.board[0][2] == "X" else GameState.O_WINS
        
        # Check for draw
        if all(cell is not None for row in self.board for cell in row):
            return GameState.DRAW
        
        return GameState.ONGOING
    
    def get_empty_cells(self) -> List[Tuple[int, int]]:
        """Get list of empty cell coordinates."""
        return [(r, c) for r in range(3) for c in range(3) 
                if self.board[r][c] is None]
    
    def reset(self):
        """Reset the board to initial state."""
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = Player.X
    
    def copy(self) -> 'GameBoard':
        """Create a deep copy of the current board state."""
        new_board = GameBoard()
        new_board.board = [row[:] for row in self.board]
        new_board.current_player = self.current_player
        return new_board