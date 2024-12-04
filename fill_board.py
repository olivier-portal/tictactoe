# from start_game_function import print_board
# choice = [2, 2, "X"]
# board = [[' ', ' ', 'O'], [' ', ' ', ' '], [' ', ' ', ' ']]
# Define player's turn and fill a box with the predefined symbol

def fill_board(board, choice):
# Updates the game board with the player symbol in the chosen box.
#:board: Game board list (3x3).
#:choice: player choice(row, column, symbol).
    row = choice[0]
    column = choice[1]
    symbol = choice[2]
    board[row - 1][column - 1] = symbol
    return board 