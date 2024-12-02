# Créer une grille de 9 cases (3x3)

def main():
# The main function
    # introduction = intro()
    board = create_grid()
    pretty = printPretty(board)
    # symbol_1, symbol_2 = sym()
    # full = isFull(board, symbol_1, symbol_2) # The function that starts the game is also in here.
    
    
def create_grid():
# This function creates a blank playboard
    print("Here is the playboard: ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]        
    return board
            

def printPretty(board):
# This function prints the board nice!
    rows = len(board)
    cols = len(board)
    print("---+---+---")
    for r in range(rows):
        print(board[r][0], " |", board[r][1], "|", board[r][2])
        print("---+---+---")
    return board

print(main())