# Créer une grille de 9 cases (3x3)

def main():
# Définir toutes fonctions pour les appeller toutes à la fin
    introduction = intro()
    players = define_players()
    board = create_grid()
    pretty = printPretty(board)
    

def intro():
    # Message de bienvenue et rappel des régles du jeu
    print("Bienvenue au jeu du morpion ! Avant de commencer une partie, relisez les règles :")
    print("\n")
    print("Dans ce jeu, deux joueurs s'affrontent. À tour de rôle, ils désignent une case et y insèrent alternativement un signe (‘X’ et ‘O’). Le premier joueur qui arrive à faire un alignement vertical, horizontal ou diagonal de trois signes gagne la partie. Si le plateau de jeu est rempli de signes et qu’il n’y a pas d'alignement de trois, alors c’est un match nul. ")
        
def define_players():
    # Définie le nom des joueurs
    print("Quel est le nom du premier joueur? ")
    player1 = (input())
    print("\n")
    print("Quel est le nom du deuxième joueur? ")
    player2 = (input())
    # ---------------------------------------------------------------------
    # Joueur 1 choisi 1 symbole, le joueur 2 est attribué automatiquement de l'autre
    symbol_1 = input(f"{player1} vous voulez jouer avec les O ou les X ? ")
    if symbol_1 == "O":
        symbol_2 = "X"
        print(f"{player2} vous jouez avec les X ! ")
    else:
        symbol_2 = "O"
        print(f"{player2} vous jouez avec les X ! ")
    
def create_grid():
# Création d'un tableau vide
    print("Commencez à jouer : ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]        
    return board
            

def printPretty(board):
# Appel du tableau et mise en page
    rows = len(board)
    cols = len(board)
    print(" ---+---+---")
    for r in range(rows):
        print("|", board[r][0], "|", board[r][1], "|", board[r][2], "|")
        print(" ---+---+---")
    return board

print(main())