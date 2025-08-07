"""
Unit tests for ai_player module.
"""

import unittest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game_logic import GameBoard, Player
from ai_player import AIPlayer, Difficulty


class TestAIPlayer(unittest.TestCase):
    """Test cases for AIPlayer class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.board = GameBoard()
        self.ai_easy = AIPlayer(Difficulty.EASY, Player.O)
        self.ai_medium = AIPlayer(Difficulty.MEDIUM, Player.O)
        self.ai_hard = AIPlayer(Difficulty.HARD, Player.O)
    
    def test_easy_ai_makes_valid_moves(self):
        """Test that easy AI makes valid moves."""
        for _ in range(10):  # Test multiple times due to randomness
            board = GameBoard()
            move = self.ai_easy.get_move(board)
            self.assertTrue(board.is_valid_move(move[0], move[1]))
    
    def test_medium_ai_wins_when_possible(self):
        """Test that medium AI takes winning moves."""
        # Set up board where O can win
        self.board.board[0][0] = "O"
        self.board.board[0][1] = "O"
        # O should play (0,2) to win
        
        move = self.ai_medium.get_move(self.board)
        self.assertEqual(move, (0, 2))
    
    def test_medium_ai_blocks_opponent(self):
        """Test that medium AI blocks opponent wins."""
        # Set up board where X is about to win
        self.board.board[0][0] = "X"
        self.board.board[0][1] = "X"
        # O should block at (0,2)
        
        move = self.ai_medium.get_move(self.board)
        self.assertEqual(move, (0, 2))
    
    def test_hard_ai_never_loses(self):
        """Test that hard AI plays optimally."""
        # Test against perfect play - hard AI should never lose
        board = GameBoard()
        ai = AIPlayer(Difficulty.HARD, Player.O)
        
        # Simulate a game where X plays optimally
        moves_x = [(1, 1), (0, 0), (2, 2)]  # Center, corner, opposite corner
        moves_o = []
        
        for i, (x_row, x_col) in enumerate(moves_x):
            if i > 0:  # O moves after first X move
                o_move = ai.get_move(board)
                moves_o.append(o_move)
                board.make_move(o_move[0], o_move[1])
            
            if board.get_game_state().value != "ongoing":
                break
                
            board.make_move(x_row, x_col)
            if board.get_game_state().value != "ongoing":
                break
        
        # Game should end in draw or O win, never X win
        final_state = board.get_game_state()
        self.assertNotEqual(final_state.value, "x_wins")
    
    def test_find_winning_move(self):
        """Test the _find_winning_move method."""
        # Set up a winning scenario
        self.board.board[0][0] = "O"
        self.board.board[0][1] = "O"
        
        winning_move = self.ai_medium._find_winning_move(self.board, "O")
        self.assertEqual(winning_move, (0, 2))
        
        # Test when no winning move exists
        empty_board = GameBoard()
        no_win = self.ai_medium._find_winning_move(empty_board, "O")
        self.assertIsNone(no_win)


if __name__ == '__main__':
    unittest.main()