def display_board(board):
    print()
    print(f' {board[7]} | {board[8]} | {board[9]} ')
    print(f'-----------')
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print(f'-----------')
    print(f' {board[1]} | {board[2]} | {board[3]} ')
    print()
    

def player_input():
    '''
    Output = (Player 1 marker, Player 2 marker)
    '''
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Choose X or O: ').upper()
        
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')
    

def place_marker(board, marker, position):
    board[position] = marker
    

def win_check(board, mark):
    # WIN TIC TAC TOE?
    # ALL ROWS, check to see match
    # ALL COLUMNS, check to see match
    # 2 DIAAGONALS, check to see match
    return ((board[1] == board[2] == board[3] == mark) or 
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or 
            (board[1] == board[4] == board[7] == mark) or
            (board[5] == board[2] == board[8] == mark) or 
            (board[9] == board[6] == board[3] == mark) or
            (board[1] == board[5] == board[9] == mark) or 
            (board[7] == board[5] == board[3] == mark))
    
import random
def choose_first():
    flip = random.randint(0,1)
    if flip == 0: 
        return 'Player 1'
    else:
        return 'Player 2'
    
def space_check(board,position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True  #Board is full

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9): '))
    return position

def replay(): #asks player whether they want to play again or not
    choice = input("Play again? (Y/N): ")
    return choice == 'Y'
    
print('Welcome to Tic-Tac-Toe!')

P1 = input('Player 1 - Enter your name: ')
P2 = input('Player 2 - Enter your name: ')
#WHILE LOOP TO KEEP RUNNING THE GAME
while True:
    
    #Play the game
    ##set the board, whos first and choosing marker
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    
    turn = choose_first()
    print(turn + ' will go first.')
    
    ## game play
    play_game = input('Ready to play? (y/n): ')
    
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    
    
    ## player1 turn
    while game_on:
        
        if turn == 'Player 1':
            #show board
            display_board(the_board)
            
            #choose a position
            position = player_choice(the_board)
            
            #place marker on position
            place_marker(the_board, player1_marker, position)
            
            #check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print(f"Player 1- {P1} WON THE GAME.....")
                game_on = False
            
            #check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME.')
                    game_on = False
                #no tie no win next player
                else:
                    turn = 'Player 2'
           
    
    ## player2 turn
        else:
            #show board
            display_board(the_board)
            
            #choose a position
            position = player_choice(the_board)
            
            #place marker on position
            place_marker(the_board, player2_marker, position)
            
            #check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print(f"Player 2 - {P2} WON THE GAME.....")
                game_on = False
            
            #check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME.')
                    game_on = False
                #no tie no win next player
                else:
                    turn = 'Player 1'
    
    if not replay():
        break

#BREAK OUT OF WHILE LOOP ON replay()