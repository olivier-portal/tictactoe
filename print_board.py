# call the board and print it
def print_board(board):
# define rows and columns
    rows = len([0, 1, 2])
    cols = len(board)
    
    
    print(" ---+---+---")
    for r in range(rows):
         print("|", board[r][0], "|", board[r][1], "|", board[r][2], "|")
         print(" ---+---+---")
    return board