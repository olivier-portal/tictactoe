# Créer un jeu de ti tac toe

def main():
# Définir toutes fonctions pour les appeller toutes à la fin
    introduction = intro()
    player1, player2 = define_players()
    symbol1, symbol2 = sym(player1, player2)
    board = create_grid()
    printBoard = print_board(board)
    

def intro():
    # Message de bienvenue et rappel des régles du jeu
    print("\n")
    print("Bienvenue au jeu du morpion ! Avant de commencer une partie, relisez les règles :")
    print("\n")
    print("Dans ce jeu, deux joueurs s'affrontent. À tour de rôle, ils désignent une case et y insèrent alternativement un signe (‘X’ et ‘O’). Le premier joueur qui arrive à faire un alignement vertical, horizontal ou diagonal de trois signes gagne la partie. Si le plateau de jeu est rempli de signes et qu’il n’y a pas d'alignement de trois, alors c’est un match nul. ")
        
def define_players():
    # Définie le nom des joueurs
    print("\n")
    print("Quel est le nom du premier joueur? ")
    player1 = (input())
    print("\n")
    print("Quel est le nom du deuxième joueur? ")
    player2 = (input())
    return player1, player2
    #  # ---------------------------------------------------------------------
    # # Joueur 1 choisi 1 symbole, le joueur 2 est attribué automatiquement de l'autre
    # symbol_1 = input(f"{player1} vous voulez jouer avec les O ou les X ? ")
    # if symbol_1 != "O" or symbol_1 !="X":
    #     input(f"{player1} vous devez choisir un O ou un X, recommencez : Voulez-vous jouer avec les O ou les X ? ")
    # elif symbol_1 == "O":
    #     symbol_2 = "X"
    #     print(f"{player2} vous jouez avec les X ! ")
    # else:
    #     symbol_2 = "O"
    #     print(f"{player1} vous jouez avec les O ! ")

def sym(player1, player2):
    # ---------------------------------------------------------------------
    # Joueur 1 choisi 1 symbole, le joueur 2 est attribué automatiquement de l'autre
    symbol_1 = ""
    while symbol_1 not in ["O", "X"]:  # Boucle jusqu'à ce qu'une entrée valide soit donnée
        symbol_1 = input(f"{player1}, voulez-vous jouer avec les O ou les X ? ").upper()
        if symbol_1 not in ["O", "X"]:
            print("Entrée invalide. Vous devez choisir entre 'O' et 'X'. Recommencez.")

    # Assigner automatiquement le symbole au joueur 2
    if symbol_1 == "O":
        symbol_2 = "X"
    else:
        symbol_2 = "O"

    print(f"\n{player1}, vous jouez avec les {symbol_1} !")
    print(f"{player2}, vous jouez avec les {symbol_2} !\n")

    return symbol_1, symbol_2
    
def create_grid():
# Création d'un tableau vide
    print("Commencez à jouer : ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]        
    return board
            

def print_board(board):
# Appel du tableau et mise en page
    rows = len(board)
    cols = len(board)
    print(" ---+---+---")
    for r in range(rows):
        print("|", board[r][0], "|", board[r][1], "|", board[r][2], "|")
        print(" ---+---+---")
    return board

print(main())