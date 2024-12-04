from start_game_function import print_board

# Define player's turn and fill a box with the predefined symbol
def fill_board(board, choice):

# Updates the game board with the player symbol in the chosen box.
#:board: Game board list (3x3).
#:choice: player choice(row, column symbol).

    row, column, symbol = choice
    board[row][column] == " "
    board[row][column] = symbol
    return board