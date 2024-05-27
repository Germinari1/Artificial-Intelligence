## Tic-Tac-Toe AI Player

This repository contains a Tic-Tac-Toe automated player game implemented using the Pygame library in Python. The game allows users to play against an AI player that uses the Minimax algorithm with Alpha-Beta pruning to make its moves.

## Description

The project consists of two main files:

1. `main.py`: This file contains the game logic and the Pygame implementation for the graphical user interface (GUI).
2. `tictactoe.py`: This file contains the implementation of the Tic-Tac-Toe game logic, including the Minimax algorithm and helper functions.

## Quick Start

To run the game, follow these steps:

1. Make sure you have Python and Pygame installed on your system.
2. Clone this repository or download the source code files.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the following command to start the game:
```python
python main.py
```
5. The game window will open, and you can choose whether to play as X or O.
6. Make your moves by clicking on the desired cells on the game board.
7. The AI player will automatically make its move after your turn.
8. The game will continue until a winner is determined or it ends in a tie.
9. Once the game is over, you can click the "Play Again" button to start a new game.

## Explanations

### `main.py`

This file handles the game loop, user input, and rendering the game board using Pygame. It imports the necessary functions from the `tictactoe.py` file to manage the game logic.

### `tictactoe.py`

This file contains the core implementation of the Tic-Tac-Toe game logic, including the following functions:

- `initial_state()`: Returns the initial empty board.
- `player(board)`: Returns the player whose turn it is based on the current board state.
- `actions(board)`: Returns a set of all possible actions (empty cell coordinates) on the current board.
- `result(board, action)`: Returns the new board state after making the specified move.
- `winner(board)`: Returns the winner (X or O) if there is one, or None if the game is still in progress or tied.
- `terminal(board)`: Returns True if the game is over (a winner or a tie), False otherwise.
- `utility(board)`: Returns the utility value (+1 for X winning, -1 for O winning, 0 for a tie) of the terminal board state.
- `minimax(board, alpha, beta)`: Implements the Minimax algorithm with Alpha-Beta pruning to determine the optimal move for the AI player.
- `max_value(board, alpha, beta)` and `min_value(board, alpha, beta)`: Helper functions used by the Minimax algorithm to evaluate the best move for the maximizing and minimizing players, respectively.

The Minimax algorithm with Alpha-Beta pruning is a decision-making algorithm used in game theory to determine the optimal move for the AI player. It explores all possible future moves and their consequences, considering both the AI player's and the opponent's optimal plays. By evaluating the utility values of the resulting board states, the algorithm can choose the move that maximizes the AI player's chances of winning or minimizes the chances of losing.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
