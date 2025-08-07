"""
Web-based Tic Tac Toe game using Flask.
"""

from flask import Flask, render_template, request, jsonify, session
import uuid
from game_logic import GameBoard, GameState, Player
from ai_player import AIPlayer, Difficulty

app = Flask(__name__)
app.secret_key = 'tic-tac-toe-secret-key'

# Store game sessions
games = {}

@app.route('/')
def index():
    """Main game page."""
    return render_template('index.html')

@app.route('/new_game', methods=['POST'])
def new_game():
    """Start a new game."""
    data = request.json
    game_id = str(uuid.uuid4())
    
    board = GameBoard()
    ai_player = None
    
    if data.get('mode') == 'ai':
        difficulty_map = {
            'easy': Difficulty.EASY,
            'medium': Difficulty.MEDIUM,
            'hard': Difficulty.HARD
        }
        difficulty = difficulty_map[data.get('difficulty', 'easy')]
        ai_player = AIPlayer(difficulty, Player.O)
    
    games[game_id] = {
        'board': board,
        'ai_player': ai_player,
        'mode': data.get('mode', 'human')
    }
    
    return jsonify({
        'game_id': game_id,
        'board': board.board,
        'current_player': board.current_player.value,
        'game_state': board.get_game_state().value
    })

@app.route('/make_move', methods=['POST'])
def make_move():
    """Make a move in the game."""
    data = request.json
    game_id = data['game_id']
    row, col = data['row'], data['col']
    
    if game_id not in games:
        return jsonify({'error': 'Game not found'}), 404
    
    game = games[game_id]
    board = game['board']
    
    # Make human move
    if not board.make_move(row, col):
        return jsonify({'error': 'Invalid move'}), 400
    
    response = {
        'board': board.board,
        'current_player': board.current_player.value,
        'game_state': board.get_game_state().value
    }
    
    # Make AI move if needed
    if (game['mode'] == 'ai' and 
        board.get_game_state() == GameState.ONGOING and 
        board.current_player == Player.O):
        
        ai_move = game['ai_player'].get_move(board)
        board.make_move(ai_move[0], ai_move[1])
        
        response.update({
            'ai_move': ai_move,
            'board': board.board,
            'current_player': board.current_player.value,
            'game_state': board.get_game_state().value
        })
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)