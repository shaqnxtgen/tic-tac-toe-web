// Tic Tac Toe Web Game JavaScript

let gameId = null;
let gameMode = null;
let difficulty = null;
let currentPlayer = 'X';
let gameState = 'ongoing';

// Game setup functions
function selectMode(mode) {
    gameMode = mode;
    
    // Update button styles
    document.querySelectorAll('.mode-btn').forEach(btn => btn.classList.remove('selected'));
    event.target.classList.add('selected');
    
    // Show/hide difficulty panel
    const difficultyPanel = document.getElementById('difficulty-panel');
    if (mode === 'ai') {
        difficultyPanel.style.display = 'block';
        difficulty = null; // Reset difficulty selection
        document.getElementById('start-game').style.display = 'none';
    } else {
        difficultyPanel.style.display = 'none';
        document.getElementById('start-game').style.display = 'block';
    }
}

function selectDifficulty(diff) {
    difficulty = diff;
    
    // Update button styles
    document.querySelectorAll('.diff-btn').forEach(btn => btn.classList.remove('selected'));
    event.target.classList.add('selected');
    
    document.getElementById('start-game').style.display = 'block';
}

async function startGame() {
    const response = await fetch('/new_game', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            mode: gameMode,
            difficulty: difficulty
        })
    });
    
    const data = await response.json();
    gameId = data.game_id;
    currentPlayer = data.current_player;
    gameState = data.game_state;
    
    // Hide setup, show game
    document.getElementById('game-setup').style.display = 'none';
    document.getElementById('game-area').style.display = 'block';
    
    createBoard();
    updateGameInfo();
}

function createBoard() {
    const board = document.getElementById('game-board');
    board.innerHTML = '';
    
    for (let i = 0; i < 9; i++) {
        const cell = document.createElement('button');
        cell.className = 'cell';
        cell.onclick = () => makeMove(Math.floor(i / 3), i % 3);
        board.appendChild(cell);
    }
}

async function makeMove(row, col) {
    if (gameState !== 'ongoing') return;
    
    const response = await fetch('/make_move', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            game_id: gameId,
            row: row,
            col: col
        })
    });
    
    if (!response.ok) {
        const error = await response.json();
        alert(error.error);
        return;
    }
    
    const data = await response.json();
    updateBoard(data.board);
    currentPlayer = data.current_player;
    gameState = data.game_state;
    
    updateGameInfo();
    
    // Show AI move if it happened
    if (data.ai_move) {
        setTimeout(() => {
            document.getElementById('game-status').textContent = 
                `AI played: ${data.ai_move[0]}, ${data.ai_move[1]}`;
        }, 500);
    }
}

function updateBoard(boardData) {
    const cells = document.querySelectorAll('.cell');
    
    for (let i = 0; i < 9; i++) {
        const row = Math.floor(i / 3);
        const col = i % 3;
        const cell = cells[i];
        const value = boardData[row][col];
        
        if (value) {
            cell.textContent = value;
            cell.className = `cell ${value.toLowerCase()}`;
            cell.disabled = true;
        } else {
            cell.textContent = '';
            cell.className = 'cell';
            cell.disabled = gameState !== 'ongoing';
        }
    }
}

function updateGameInfo() {
    const playerDiv = document.getElementById('current-player');
    const statusDiv = document.getElementById('game-status');
    
    if (gameState === 'ongoing') {
        playerDiv.textContent = `Current Player: ${currentPlayer}`;
        statusDiv.textContent = gameMode === 'ai' && currentPlayer === 'O' ? 
            'AI is thinking...' : '';
    } else {
        playerDiv.textContent = '';
        
        if (gameState === 'x_wins') {
            statusDiv.textContent = '🎉 Player X Wins! 🎉';
            statusDiv.className = 'winner';
        } else if (gameState === 'o_wins') {
            statusDiv.textContent = gameMode === 'ai' ? 
                '🤖 AI Wins! 🤖' : '🎉 Player O Wins! 🎉';
            statusDiv.className = 'winner';
        } else if (gameState === 'draw') {
            statusDiv.textContent = '🤝 It\'s a Draw! 🤝';
        }
    }
}

function newGame() {
    startGame();
}

function resetSetup() {
    document.getElementById('game-area').style.display = 'none';
    document.getElementById('game-setup').style.display = 'block';
    
    // Reset selections
    document.querySelectorAll('.mode-btn, .diff-btn').forEach(btn => 
        btn.classList.remove('selected'));
    document.getElementById('difficulty-panel').style.display = 'none';
    document.getElementById('start-game').style.display = 'none';
    
    gameMode = null;
    difficulty = null;
    gameId = null;
}