# Créer un jeu de ti tac toe

def main():
    """
    La fonction main() intègre les fonctions principales dans des variables pour les appeller toutes à la fin
    Cette fonction permet aussi de garder en mémoire tampon les variables qui seront utlisable en arguments dans una autre fonction 
    
    Exemple: La fonction define-player() définie le nom des 2 joueurs, elle retourne le nom du joueur 1 dans la variable player1
             et le nom du joueur 2 dans la variable player2
             les variables player1 et player2 sont stockées et utilisables en tant qu'argument dans la fonction d'attribution des symboles X ou O => sym(player1, player2)
    """
    introduction = intro()
    player1, player2 = define_players()
    symbol_1, symbol_2 = sym(player1, player2)
    board = create_grid()
    printBoard = print_board(board)
    fillBoard = fill_board(board, player1, player2, symbol_1, symbol_2)
    

def intro():
    # Message de bienvenue et rappel des régles du jeu
    print("\n")
    print("Bienvenue au jeu du morpion ! Avant de commencer une partie, relisez les règles :")
    print("\n")
    print("Dans ce jeu, deux joueurs s'affrontent. À tour de rôle, ils désignent une case et y insèrent alternativement un signe (‘X’ et ‘O’). Le premier joueur qui arrive à faire un alignement vertical, horizontal ou diagonal de trois signes gagne la partie. Si le plateau de jeu est rempli de signes et qu’il n’y a pas d'alignement de trois, alors c’est un match nul. ")
        
def define_players():
    # Définie le nom des joueurs
    player1 = (input("\nQuel est le nom du premier joueur? ")) # Définie le nom du premier joueur
    player2 = (input("\nQuel est le nom du deuxième joueur? ")) # Définie le nom du deuxième joueur
    
    return player1, player2 #Renvoie et mémorise les noms des joueurs dans la variables du main

def sym(player1, player2):
    # ---------------------------------------------------------------------
    # Joueur 1 choisi 1 symbole, le joueur 2 est attribué automatiquement de l'autre
    symbol_1 = ""
    while symbol_1 not in ["O", "X"]:  # Boucle jusqu'à ce qu'une entrée valide soit donnée
        symbol_1 = input(f"\n{player1}, voulez-vous jouer avec les O ou les X ? ").upper()
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

def fill_board(board, player1, player2, symbol_1, symbol_2):
    choice = input(f"\n{player1} à vous de jouer, choisissez une case entre 1 et 9 : ")
    if choice == 1:
        board[0][0] == symbol_1         
        print(print_board(board))
        #     print(" ---+---+---")
        # for r in range(rows):
        #     for c in range(cols):
        #         print("|", board[r][c], "|", board[r][c], "|", board[r][c], "|")
        #         print(" ---+---+---")
        # return board
    # elif symbol_1 == "2":
    #     return board[0][1] == symbol_1
    # elif symbol_1 == "3":
    #     return board[0][2] == symbol_1
    # elif symbol_1 == "4":
    #     return board[1][0] == symbol_1
    # elif symbol_1 == "5":
    #     return board[1][1] == symbol_1
    # elif symbol_1 == "6":
    #     return board[1][2] == symbol_1
    # elif symbol_1 == "7":
    #     return board[2][0] == symbol_1
    # elif symbol_1 == "8":
    #     return board[2][1] == symbol_1
    # elif symbol_1 == "9":
    #     return board[2][0] == symbol_1
    
    return board


print(main())