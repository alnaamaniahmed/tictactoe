import random

# Function to display the Tic Tac Toe board
def display_board(board):
    print('\n' * 100)
    print('   ' + board[7] + '   |   ' + board[8] + '   |   ' + board[9] + '')
    print('-------|-------|-------')
    print('   ' + board[4] + '   |   ' + board[5] + '   |   ' + board[6] + '')
    print('-------|-------|-------')
    print('   ' + board[1] + '   |   ' + board[2] + '   |   ' + board[3] + '')
    print('-------|-------|-------')

# Function to let a player choose their marker (X or O)
def player_input():
    markerXO = ''
    while not(markerXO == 'X' or markerXO == 'O'):
        markerXO = input('Do you want to be X or O?').upper()
    if markerXO == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# Function to place a marker on the board
def place_marker(board, marker, position):
    board[position] = marker

# Function to check if a player has won
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark))

# Function to randomly choose which player goes first
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

# Function to check if a space on the board is available
def space_check(board, position):
    return board[position] == ' '

# Function to check if the board is full
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

# Function to let a player choose their next move
def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Choose your position from (1-9)"))
    return position

# Function to ask if players want to play again
def replay():
    return input('Do you want to play again (Yes/No)').lower().startswith('y')


# Main game loop
print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board for a new game
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + " will go first")
    play_game = input('Are you ready to play? Yes/No')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player 1's turn
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)
            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print("Player 1 has won the game!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("It's a draw!")
                    break
                else:
                    turn = "Player 2"
        else:
            # Player 2's turn
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)
            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print("Player 2 has won the game!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("It's a draw!")
                    break
                else:
                    turn = "Player 1"

    if not replay():
        break
