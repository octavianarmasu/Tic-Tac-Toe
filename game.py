
def display_board(board):
    
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[1]+'|'+board[2]+'|'+board[3])

def player_input():
    
    marker = ''
    
    while marker != 'X' and marker !='O':
        marker = input("Player 1, choose X or O: ")
        
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
        
    return (player1,player2)

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    if mark == board[1] and board[1] == board[2] and board[1] == board[3]:
        return True
    if mark == board[1] and board[1] == board[5] and board[1] == board[9]:
        return True
    if mark == board[1] and board[1] == board[4] and board[1] == board[7]:
        return True
    if mark == board[3] and board[3] == board[6] and board[3] == board[9]:
        return True
    if mark == board[3] and board[3] == board[5] and board[3] == board[7]:
        return True
    if mark == board[4] and board[4] == board[5] and board[4] == board[6]:
        return True
    if mark == board[7] and board[7] == board[8] and board[8] == board[9]:
        return True
    if mark == board[2] and board[2] == board[5] and board[2] == board[8]:
        return True
    return False

import random

def choose_first():
    number = random.randint(1,2)
    if number == 1:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    if board[position] == ' ':
        return True
    return False

def full_board_check(board):
    contor = 0
    for item in board:
        if item == ' ' and contor != 0:
            return False
        contor += 1
    return True

def player_choice(board):
    position = ' '
    while position not in range(1,10):
        position = int(input("Please choose a position (1-9): "))
        if position in range (1,10) and space_check(board, position):
            return position
        else:
            position = ' '

def replay():
    mess = ' '
    while mess != 'Yes' and mess != 'No':
        mess = input("Do you want to play again? (Yes or No): ")
        
    if mess == 'Yes':
        return True
    return False

print('Welcome to Tic Tac Toe!')

while True:
        
    board = [' '] * 10
    player1, player2 = player_input()
    if choose_first() == 'Player 1':
        print('Player 1 is starting')
        start = 1
    else:
        print('Player 2 is starting')
        start = 2
        
    while full_board_check(board) == False and win_check(board, 'X') == False and win_check(board,'O') == False:
        if start == 1:
            position = player_choice(board)
            place_marker(board, player1, position)
            display_board(board)
            start = 2
        else:
            position = player_choice(board)
            place_marker(board, player2, position)
            display_board(board)
            start = 1
                                  
    if win_check(board, player1):
        print("Player 1 won!")
    elif win_check(board, player2):
        print("Player 2 won!")
    if full_board_check(board):
        print("Tie!")

    if not replay():
        break