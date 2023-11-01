
import math

# takes in the num_row and num_cols from user input and sets each spot in the list to “-”
def initialize_board(num_rows, num_cols):
    board = [
        ["-" for i in range(num_cols)] for e in range(num_rows)
    ]

    return board

# takes in 2D character list for the board and prints board
def print_board(board):
    board_copy = [' '.join(k) for k in board]
    new = ('\n'.join([str(lst) for lst in board_copy]))
    print(new)

# places token in the column that the user has chosen
def insert_chip(board, col, chip_type):
    global c
    c = col
    global row
    row = 0
    # moves down a row if the row in the column is occupied by a token
    for h in board:
        if h[col] == 'o' or h[col] == 'x':
            row += 1

        else:
            row = row

    # prints board with the new chip added
    if col in range(0, cols):

        if board[row][col] == 'x' or board[row][col] == 'o':
            board[row][col] = chip_type
            print_board(reversed(board))

        else:
            board[row][col] = chip_type
            print_board(reversed(board))

    return row

# checks if the token in this location, of the specified chip type, creates four in a row
def check_if_winner(board, col, row, chip_type):

    count = 1
    increment = 1

    # checks for four tokens in a row horizontally and returns true if found
    for c in range(0, len(board[row])):

        if board[row][0] == board[row][0 + increment]:
            count += 1
            increment += 1
            if count >= 4:
                return True
        else:
            count = 1

    index1 = 1
    count1 = 1

    # checks for four tokens in a row vertically and returns true if found
    for i in range(1, 4):
        if board[row - index1][col] == chip_type:
            count1 += 1
            index1 += 1
            if count1 >= 4:
                return True
        else:
            count1 = 1

    return False

# checks to see if there are any spots with a value of '-', returns true if the board is not empty
def full_board(board):

    for r in board:
        if '-' in r:
            return False
    return True

if __name__ == "__main__":

    # prompts the user for inputs witch are assigned to the amount of rows and columns in the board respectively
    rows = int(input("What would you like the height of the board to be?"))
    cols = int(input("What would you like the length of the board to be?"))

    # sets a variable up equal to the function the generates the list prior to getting printed and formatted
    board1 = initialize_board(rows, cols)

    # calls the function and prints the board in reverse
    print_board(initialize_board(rows, cols))

    print('\nPlayer 1: x\nPlayer 2: o')

    # sets the variable equal to the amount of times the loop should be repeated for the game
    game_length = math.ceil((rows * cols) / 2)

    for g in range(game_length):

        # inserts the x in the column requested by the user
        insert_chip(board1, col=int(input("\nPlayer 1: Which column would you like to choose?")), chip_type='x')

        # if winner function returns True player 1 wins and the loop is broken out of
        if check_if_winner(board1, c, row, chip_type='x'):
            print("\nPlayer 1 won the game!")
            break

        # checks if the board is full, if False loop continues, if it True there is a draw
        if full_board(board1):
            print("Draw. Nobody wins.")
            break

        # inserts the o in the column requested by the user
        insert_chip(board1, col=int(input("\nPlayer 2: Which column would you like to choose?")), chip_type='o')

        # if winner function returns True player 2 wins and the loop is broken out of
        if check_if_winner(board1, c, row, chip_type='o'):
            print("\nPlayer 2 won the game!")
            break

        # checks if the board is full, if False loop continues, if it True there is a draw
        if full_board(board1):
            print("Draw. Nobody wins.")
            break
