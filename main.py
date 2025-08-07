#!/usr/bin/env python3
"""
Main entry point for the Tic Tac Toe game.

This module serves as the entry point for the application and handles
command-line arguments for different game modes.
"""

import sys
import argparse
from cli_interface import CLIInterface


def main():
    """Main function to start the Tic Tac Toe game."""
    parser = argparse.ArgumentParser(
        description="Tic Tac Toe - A classic game with AI opponents",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py              # Start interactive game
  python main.py --help       # Show this help message

Game Features:
  • Human vs Human mode
  • Human vs AI mode with 3 difficulty levels
  • Colorful CLI interface
  • Input validation and error handling
        """
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='Tic Tac Toe v1.0.0'
    )
    
    args = parser.parse_args()
    
    try:
        # Start the game
        game = CLIInterface()
        game.run_game()
        
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Goodbye! 👋")
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()