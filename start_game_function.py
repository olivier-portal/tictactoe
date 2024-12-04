# Introduction: Welcome players and remind rules
def intro():
    # Welcome message
    print("\nBienvenue au jeu du morpion ! Avant de commencer une partie, lisez les règles :")
    
    # Remind rules
    print("\nDans ce jeu, deux joueurs s'affrontent. À tour de rôle, ils désignent une case et y insèrent alternativement un signe (‘X’ et ‘O’). Le premier joueur qui arrive à faire un alignement vertical, horizontal ou diagonal de trois signes gagne la partie. Si le plateau de jeu est rempli de signes et qu’il n’y a pas d'alignement de trois, alors c’est un match nul. ")
 
# Define players' names       
def define_players():
    player1 = [(input("\nQuel est le nom du premier joueur? ")), ""] # Define player1 name
    player2 = [(input("\nQuel est le nom du deuxième joueur? ")), ""] # Define player2 name
    
    return player1, player2 #Return and stock player1 and player2 in main() fonction variable

#Attribute a symbol to each player
def define_symbol(player1, player2):
    # ---------------------------------------------------------------------
    # player1 choose a symbol, the other symbol is automatically attributed to player2
    symbol_1 = ""
    while symbol_1 not in ["O", "X"]:  # Loop until valid input is given
        
        symbol_1 = input(f"\n{player1[0]}, voulez-vous jouer avec les O ou les X ? ").upper()
        #player1 chooses a symbol and uppercase / lowercase are handeled
        
        if symbol_1 not in ["O", "X"]:
            print("Entrée invalide. Vous devez choisir entre 'O' et 'X'. Recommencez.")
        # if char is out of range => return error message + start the loop again

    # player1 chooses a symbol and it assigns automatically the left symbol to player2
    if symbol_1 == "O":
        player1[1] = "O"
        player2[1] = "X"
        
    else:
        player2[1] = "O"
        player1[1] = "X"        
    
    print(f"\n{player1[0]}, vous jouez avec les {player1[1]} !")
    print(f"{player2[0]}, vous jouez avec les {player2[1]} !\n")

    return player1[1], player2[1]

# Create an empty tic tac toe board
def create_grid():
    # print("Commencez à jouer : ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]        
    return board
            
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