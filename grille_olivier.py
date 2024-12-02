# Créer une grille de 9 cases (3x3)

def main():
# The main function
    introduction = intro()
    board = create_grid()
    pretty = printPretty(board)
    # symbol_1, symbol_2 = sym()
    # full = isFull(board, symbol_1, symbol_2) # The function that starts the game is also in here.

def intro():
    print("Bienvenue au jeu du morpion ! Avant de commencer une partie, entrons le nom des joueurs :")
    print("\n")
    print("Quel est le nom du premier joueur? ")
    player1 = (input())
    print("\n")
    print("Quel est le nom du deuxième joueur? ")
    player2 = (input())
    symbol_1 = input(f"{player1} vous voulez jouer avec les O ou les X ? ")
    if symbol_1 == "O":
        symbol_2 = "X"
        print(f"{player2} vous jouez avec les X ! ")
    else:
        symbol_2 = "O"
        print(f"{player2} vous jouez avec les X ! ")
    
    
# def sym():
#     symbol_1 = input(f"{player1} vous voulez jouer avec les O ou les X ? ")
#     if symbol_1 == "O":
#         symbol_2 = "X"
#         print(f"{player2} vous jouez avec les X ! ")
#     else:
#         symbol_2 = "O"
#         print(f"{player2} vous jouez avec les X ! ")
    
def create_grid():
# This function creates a blank playboard
    print("Commencez à jouer : ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]        
    return board
            

def printPretty(board):
# This function prints the board nice!
    rows = len(board)
    cols = len(board)
    print(" ---+---+---")
    for r in range(rows):
        print("|", board[r][0], "|", board[r][1], "|", board[r][2], "|")
        print(" ---+---+---")
    return board

print(main())