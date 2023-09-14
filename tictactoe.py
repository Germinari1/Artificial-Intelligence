"""
Tic Tac Toe Player
"""

import math
import copy

#possible moves
X = "X"
O = "O"
EMPTY = None

#lenght of row/column
LEN = 3

def initial_state():
    """
    Returns starting board of the board. -> empyy board
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #set counters for moves
    counter_O = 0
    counter_X =0

    #iterate over board and count moves
    for x in range(0, LEN):
        for y in range(0, LEN):
            if board[x][y] == 'O':
                counter_O +=1
            elif board[x][y] == 'X':
                counter_X +=1

    #decide turn (X starts game)
    if counter_X > counter_O:
        return 'O'
    else:
        return 'X'



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board at current board
    """
    # return set for actions f.
    acts = set()

    #iterate over board
    for x in range(LEN):
        for y in range(LEN):
            if board[x][y] == EMPTY:
                acts.add((x,y))

    #possible actions = spot in which there is no 'X' nor 'O'
    return acts



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #check for move validity
    if action not in actions(board):
        raise Exception('That is not a legal move.')

    #create copy of board and apply move
    new_board = copy.deepcopy(board)
    i,j = action
    new_board[i][j] = player(board)

    return new_board


def winner(board, match=None):
    """
    Returns the winner of the game, if there is one.
    """
    #check row
    if ['X']*3 in board:
        return 'X'
    elif ['O']*3 in board:
        return 'O'

    #check column
    for x in range(LEN):
        for y in range(LEN):
            #if board[x][y] == board[x+1][y] == board[x+2][y]:
            if board[x][y] == board[(x+1)%LEN][y] == board[(x+2)%LEN][y]:
                return board[x][y]

    #check diagonals
    # Check top left to bottom right diagonal
    for x in range(LEN):
        #if board[x][x] == board[x+1][x+1] == board[x+2][x+2]:
        if board[x][x] == board[(x+1)%LEN][(x+1)%LEN] == board[(x+2)%LEN][(x+2)%LEN]:
            return board[x][x]

    # Check top right to bottom left diagonal
    for x in range(LEN):
        #if board[x][LEN-1-x] == board[x+1][LEN-2-x] == board[x+2][LEN-3-x]:
        if board[x][LEN-1-x] == board[(x+1)%LEN][LEN-1-(x+1)%LEN] == board[(x+2)%LEN][LEN-1-(x+2)%LEN]:
            return board[x][LEN-1-x]

    #return None if no winning board was achieved (tie or game in progress)
    return None


def terminal(board): ###CHECK
    """
    Returns True if game is over, False otherwise.
    """
    #case 1: X or O win
    if winner(board) in ['X', 'O']:
        return True

    #case 2: game in progress
    for x in range(LEN):
        for y in range(LEN):
            if board[x][y] == EMPTY:
                return False

    #case 3: tie
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise. => outputs utility of the board
    """
    #map value returned by winner() with the associated utility
    winner_utility = {
        'X': 1,
        'O': -1,
        None: 0
        }

    if terminal(board):
        return winner_utility[winner(board)]
    else:
        raise Exception('Only applicable for terminal states.')

def minimax_vals(board):
    """
    returns the board that maximizes or minimizes the utility, depending on the agent`s turn
    recursive approach
    """
    #end game case
    if terminal(board):
        return utility(board)

    if player(board) != 'X':  #player O
        f = min
        v = math.inf
    #set appropriate function and variable depending on how plays now
    else:
        f = max
        v = - math.inf

    #iterate over possible actions and choose optmal value
    for act in actions(board):
        v = f(v, minimax_vals(result(board, act)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #case: terminal board
    if terminal(board):
        return True

    for act in actions(board):
        if minimax_vals(board) == minimax_vals(result(board, act)): #iterate over possible actions and choose the one that mathces with minimax_vals, that is, that encodes the optimal value
            return act



