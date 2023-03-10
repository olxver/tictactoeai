import os    
import time    
    
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

player = 1    
   
########win Flags##########    
Win = 1    
Draw = -1    
Running = 0    
Stop = 1    
###########################    
Game = Running    
Mark = 'X'    
   
#This Function Draws Game Board    
def DrawBoard():    
    print(" %c | %c | %c " % (board[1],board[2],board[3]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[4],board[5],board[6]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[7],board[8],board[9]))    
    print("   |   |   ")    
   
#This Function Checks position is empty or not    
def CheckPosition(x):    
    if(board[x] == ' '):    
        return True    
    else:    
        return False    
   
#This Function Checks player has won or not    
def check_win(board):
    # Check rows
    for i in range(1, 8, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return board[i]

    # Check columns
    for i in range(1, 4):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return board[i]

    # Check diagonals
    if board[1] == board[5] == board[9] != ' ':
        return board[1]
    if board[3] == board[5] == board[7] != ' ':
        return board[3]

    # Check for tie
    if ' ' not in board.values():
        return 'Tie'

    # No winner yet
    return None

import random

def evaluate(board):
    # Check rows for a win
    for i in range(0, 9, 3):
        if board[i] == board[i+1] and board[i+1] == board[i+2]:
            if board[i] == 'X':
                return 10
            elif board[i] == 'O':
                return -10
    
    # Check columns for a win
    for i in range(3):
        if board[i] == board[i+3] and board[i+3] == board[i+6]:
            if board[i] == 'X':
                return 10
            elif board[i] == 'O':
                return -10
    
    # Check diagonals for a win
    if board[0] == board[4] and board[4] == board[8]:
        if board[0] == 'X':
            return 10
        elif board[0] == 'O':
            return -10
    
    if board[2] == board[4] and board[4] == board[6]:
        if board[2] == 'X':
            return 10
        elif board[2] == 'O':
            return -10
    
    # If no one wins, return 0
    return 0

def get_moves(board):
    """
    This function returns a list of available moves on the board.
    """
    moves = []
    for i in range(1, 10):
        if board[i] == ' ':
            moves.append(i)
    return moves
# The main algorithm for the game

def minimax(board, player, depth):
    # Base case: check for winner or tie
    winner = check_win(board)
    if winner:
        if winner == 'X':
            return -10 + depth, None
        elif winner == 'O':
            return 10 - depth, None
        else:
            return 0, None

    # Recursive case: evaluate all possible moves and choose the best one
    if player == 2:  # Player 2 is 'O'
        best_score = -1000
        best_move = None
        for move in get_moves(board):
            board[move] = 'O'
            score, _ = minimax(board, 1, depth+1)
            board[move] = ' '
            if score > best_score:
                best_score = score
                best_move = move
        return best_score, best_move
    else:  # Player 1 is 'X'
        best_score = 1000
        best_move = None
        for move in get_moves(board):
            board[move] = 'X'
            score, _ = minimax(board, 2, depth+1)
            board[move] = ' '
            if score < best_score:
                best_score = score
                best_move = move
        return best_score, best_move

# Main game loop
while(Game == Running):
    os.system('clear')
    DrawBoard()
    if(player % 2 != 0):
        print("Player 1's turn")
        Mark = 'X'
        choice = int(input("Enter the position between [1-9] where you want to mark : "))
        if(CheckPosition(choice)):
            board[choice] = Mark
            player+=1
            if check_win(board) or len(get_moves(board)) == 0:
                Game = not Running
    else:
        print("AI's turn")
        Mark = 'O'
        _, choice = minimax(board, 2, 0)
        if choice is None:
            print("")
            Game = not Running
        else:
            board[choice] = Mark
            player+=1
            if check_win(board) or len(get_moves(board)) == 0:
                Game = not Running
    time.sleep(1)




os.system('clear')    
DrawBoard()    
if(Game==Draw):    
    print("no one won lol")    
elif(Game==Win):    
    player-=1    
    if(player%2!=0):    
        print("wow player 1 won")    
    else:    
        print("how do you lose to an ai?")
