"""
Unit tests for game_logic module.
"""

import unittest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game_logic import GameBoard, Player, GameState


class TestGameBoard(unittest.TestCase):
    """Test cases for GameBoard class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.board = GameBoard()
    
    def test_initial_state(self):
        """Test initial board state."""
        self.assertEqual(self.board.current_player, Player.X)
        self.assertEqual(self.board.get_game_state(), GameState.ONGOING)
        self.assertEqual(len(self.board.get_empty_cells()), 9)
    
    def test_valid_move(self):
        """Test making valid moves."""
        self.assertTrue(self.board.make_move(0, 0))
        self.assertEqual(self.board.board[0][0], "X")
        self.assertEqual(self.board.current_player, Player.O)
    
    def test_invalid_move(self):
        """Test invalid moves."""
        self.board.make_move(0, 0)
        self.assertFalse(self.board.make_move(0, 0))  # Same position
        self.assertFalse(self.board.make_move(-1, 0))  # Out of bounds
        self.assertFalse(self.board.make_move(3, 0))   # Out of bounds
    
    def test_win_conditions(self):
        """Test various win conditions."""
        # Test row win
        self.board.make_move(0, 0)  # X
        self.board.make_move(1, 0)  # O
        self.board.make_move(0, 1)  # X
        self.board.make_move(1, 1)  # O
        self.board.make_move(0, 2)  # X wins
        self.assertEqual(self.board.get_game_state(), GameState.X_WINS)
    
    def test_draw_condition(self):
        """Test draw condition."""
        moves = [(0,0), (0,1), (0,2), (1,1), (1,0), (1,2), (2,1), (2,0), (2,2)]
        for row, col in moves:
            self.board.make_move(row, col)
        self.assertEqual(self.board.get_game_state(), GameState.DRAW)
    
    def test_copy(self):
        """Test board copying."""
        self.board.make_move(0, 0)
        copied_board = self.board.copy()
        
        self.assertEqual(copied_board.board[0][0], "X")
        self.assertEqual(copied_board.current_player, Player.O)
        
        # Ensure it's a deep copy
        copied_board.make_move(1, 1)
        self.assertIsNone(self.board.board[1][1])
    
    def test_reset(self):
        """Test board reset."""
        self.board.make_move(0, 0)
        self.board.reset()
        
        self.assertEqual(self.board.current_player, Player.X)
        self.assertEqual(len(self.board.get_empty_cells()), 9)
        self.assertIsNone(self.board.board[0][0])


if __name__ == '__main__':
    unittest.main()