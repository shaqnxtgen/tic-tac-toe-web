"""
Command-line interface for Tic Tac Toe game.

This module provides a text-based interface with colored output and
user-friendly prompts for an engaging game experience.
"""

import os
from typing import Tuple
from game_logic import GameBoard, GameState, Player
from ai_player import AIPlayer, Difficulty


class Colors:
    """ANSI color codes for terminal output."""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'


class CLIInterface:
    """
    Command-line interface for the Tic Tac Toe game.
    
    Provides methods for displaying the board, getting user input,
    and managing the game flow with colored output.
    """
    
    def __init__(self):
        """Initialize the CLI interface."""
        self.board = GameBoard()
        self.ai_player = None
        self.game_mode = None
    
    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_title(self):
        """Display the game title."""
        title = f"""
{Colors.CYAN}{Colors.BOLD}
╔══════════════════════════════════╗
║           TIC TAC TOE            ║
║         Python Edition           ║
╚══════════════════════════════════╝
{Colors.END}"""
        print(title)
    
    def display_board(self):
        """Display the current game board with colors."""
        print(f"\n{Colors.BOLD}Current Board:{Colors.END}")
        print(f"{Colors.YELLOW}   0   1   2{Colors.END}")
        
        for i, row in enumerate(self.board.board):
            row_display = f"{Colors.YELLOW}{i}{Colors.END}  "
            for j, cell in enumerate(row):
                if cell == "X":
                    symbol = f"{Colors.RED}{Colors.BOLD}X{Colors.END}"
                elif cell == "O":
                    symbol = f"{Colors.BLUE}{Colors.BOLD}O{Colors.END}"
                else:
                    symbol = " "
                
                row_display += symbol
                if j < 2:
                    row_display += f"{Colors.WHITE} | {Colors.END}"
            
            print(row_display)
            if i < 2:
                print(f"{Colors.WHITE}  ---|---|---{Colors.END}")
    
    def get_game_mode(self) -> str:
        """Get the game mode from user."""
        while True:
            print(f"\n{Colors.BOLD}Select Game Mode:{Colors.END}")
            print(f"{Colors.GREEN}1.{Colors.END} Human vs Computer")
            print(f"{Colors.GREEN}2.{Colors.END} Human vs Human")
            
            choice = input(f"\n{Colors.CYAN}Enter your choice (1-2): {Colors.END}").strip()
            
            if choice == "1":
                return "human_vs_ai"
            elif choice == "2":
                return "human_vs_human"
            else:
                print(f"{Colors.RED}Invalid choice! Please enter 1 or 2.{Colors.END}")
    
    def get_difficulty(self) -> Difficulty:
        """Get AI difficulty level from user."""
        while True:
            print(f"\n{Colors.BOLD}Select Difficulty:{Colors.END}")
            print(f"{Colors.GREEN}1.{Colors.END} Easy (Random moves)")
            print(f"{Colors.YELLOW}2.{Colors.END} Medium (Basic strategy)")
            print(f"{Colors.RED}3.{Colors.END} Hard (Unbeatable)")
            
            choice = input(f"\n{Colors.CYAN}Enter difficulty (1-3): {Colors.END}").strip()
            
            if choice == "1":
                return Difficulty.EASY
            elif choice == "2":
                return Difficulty.MEDIUM
            elif choice == "3":
                return Difficulty.HARD
            else:
                print(f"{Colors.RED}Invalid choice! Please enter 1, 2, or 3.{Colors.END}")
    
    def get_player_move(self, player_name: str) -> Tuple[int, int]:
        """
        Get move coordinates from human player.
        
        Args:
            player_name: Name of the current player
            
        Returns:
            Tuple of (row, col) coordinates
        """
        while True:
            try:
                move_input = input(f"\n{Colors.BOLD}{player_name}'s turn{Colors.END} "
                                 f"(format: row,col or row col): ").strip()
                
                # Parse input (support both "1,2" and "1 2" formats)
                if ',' in move_input:
                    row, col = map(int, move_input.split(','))
                else:
                    row, col = map(int, move_input.split())
                
                if self.board.is_valid_move(row, col):
                    return (row, col)
                else:
                    print(f"{Colors.RED}Invalid move! Cell is already occupied or out of bounds.{Colors.END}")
                    
            except (ValueError, IndexError):
                print(f"{Colors.RED}Invalid format! Please enter row,col (e.g., 1,2) or row col (e.g., 1 2).{Colors.END}")
            except KeyboardInterrupt:
                print(f"\n{Colors.YELLOW}Game interrupted. Goodbye!{Colors.END}")
                exit(0)
    
    def display_game_result(self, state: GameState):
        """Display the final game result."""
        if state == GameState.X_WINS:
            print(f"\n{Colors.GREEN}{Colors.BOLD}🎉 Player X wins! 🎉{Colors.END}")
        elif state == GameState.O_WINS:
            print(f"\n{Colors.GREEN}{Colors.BOLD}🎉 Player O wins! 🎉{Colors.END}")
        elif state == GameState.DRAW:
            print(f"\n{Colors.YELLOW}{Colors.BOLD}🤝 It's a draw! 🤝{Colors.END}")
    
    def play_again(self) -> bool:
        """Ask if user wants to play again."""
        while True:
            choice = input(f"\n{Colors.CYAN}Play again? (y/n): {Colors.END}").strip().lower()
            if choice in ['y', 'yes']:
                return True
            elif choice in ['n', 'no']:
                return False
            else:
                print(f"{Colors.RED}Please enter 'y' for yes or 'n' for no.{Colors.END}")
    
    def run_game(self):
        """Main game loop."""
        self.clear_screen()
        self.display_title()
        
        while True:
            # Setup game
            self.game_mode = self.get_game_mode()
            
            if self.game_mode == "human_vs_ai":
                difficulty = self.get_difficulty()
                self.ai_player = AIPlayer(difficulty, Player.O)
                print(f"\n{Colors.GREEN}Game started! You are X, Computer is O.{Colors.END}")
            else:
                print(f"\n{Colors.GREEN}Game started! Player 1 is X, Player 2 is O.{Colors.END}")
            
            # Game loop
            while True:
                self.display_board()
                state = self.board.get_game_state()
                
                if state != GameState.ONGOING:
                    self.display_game_result(state)
                    break
                
                # Get current player move
                if self.board.current_player == Player.X:
                    if self.game_mode == "human_vs_ai":
                        row, col = self.get_player_move("You (X)")
                    else:
                        row, col = self.get_player_move("Player 1 (X)")
                else:
                    if self.game_mode == "human_vs_ai":
                        print(f"\n{Colors.MAGENTA}Computer is thinking...{Colors.END}")
                        row, col = self.ai_player.get_move(self.board)
                        print(f"{Colors.MAGENTA}Computer plays: {row},{col}{Colors.END}")
                    else:
                        row, col = self.get_player_move("Player 2 (O)")
                
                # Make the move
                self.board.make_move(row, col)
            
            # Ask to play again
            if not self.play_again():
                break
            
            # Reset for new game
            self.board.reset()
            self.clear_screen()
            self.display_title()
        
        print(f"\n{Colors.CYAN}Thanks for playing! Goodbye! 👋{Colors.END}")


if __name__ == "__main__":
    game = CLIInterface()
    game.run_game()