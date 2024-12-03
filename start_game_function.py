# Create a tic tac toe game

def start_game():
    """
    The main() function stocks the principal functions in variables in order to call them at the end
    This function also allows you to keep in buffer the variables which will be used as arguments in another function 
    
    Example: The define-player() function defines the name of the 2 players, it returns the name of player 1 in the variable player1
             and the name of player 2 in the variable player2
             the player1 and player2 variables are stored and used as arguments in the symbol allocation function (X or O)
             => sym(player1, player2)
    """
    introduction = intro()
    player1, player2 = define_players()
    symbol_1, symbol_2 = define_symbol(player1, player2)
    board = create_grid()
    printBoard = print_board(board)
    
# Introduction: Welcome players and remind rules
def intro():
    # Welcome message
    print("\nBienvenue au jeu du morpion ! Avant de commencer une partie, lisez les règles :")
    
    # Remind rules
    print("\nDans ce jeu, deux joueurs s'affrontent. À tour de rôle, ils désignent une case et y insèrent alternativement un signe (‘X’ et ‘O’). Le premier joueur qui arrive à faire un alignement vertical, horizontal ou diagonal de trois signes gagne la partie. Si le plateau de jeu est rempli de signes et qu’il n’y a pas d'alignement de trois, alors c’est un match nul. ")
 
# Define players' names       
def define_players():
    player1 = (input("\nQuel est le nom du premier joueur? ")) # Define player1 name
    player2 = (input("\nQuel est le nom du deuxième joueur? ")) # Define player2 name
    
    return player1, player2 #Return and stock player1 and player2 in main() fonction variable

#Attribute a symbol to each player
def define_symbol(player1, player2):
    # ---------------------------------------------------------------------
    # player1 choose a symbol, the other symbol is automatically attributed to player2
    symbol_1 = ""
    while symbol_1 not in ["O", "X"]:  # Loop until valid input is given
        
        symbol_1 = input(f"\n{player1}, voulez-vous jouer avec les O ou les X ? ").upper()
        #player1 chooses a symbol and uppercase / lowercase are handeled
        
        if symbol_1 not in ["O", "X"]:
            print("Entrée invalide. Vous devez choisir entre 'O' et 'X'. Recommencez.")
        # if char is out of range => return error message + start the loop again

    # player1 chooses a symbol and it assign automatically the left symbol to player2
    if symbol_1 == "O":
        symbol_2 = "X"
    else:
        symbol_2 = "O"

    print(f"\n{player1}, vous jouez avec les {symbol_1} !")
    print(f"{player2}, vous jouez avec les {symbol_2} !\n")

    return symbol_1, symbol_2

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