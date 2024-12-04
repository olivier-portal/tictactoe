def choose_box(board, player1, player2, symbol_1, symbol_2):
    # Define who starts first:
    count = 1
    if count % 2 == 0:
        actual_player = player2
    else:
        actual_player = player1
    assigned_symbol = actual_player[1]
    print(f"\n{actual_player[0]} c'est votre tour de jouer ! ")
    
    # Ask player to choose a row
    row = ""
    
    # While row entry is out of range return error
    while row not in [1, 2, 3]:
        row = int(input(f"\nChoisissez une ligne entre 1 et 3 : ")) #row OK
    
        if row not in [1, 2, 3]:
            print("Entrée invalide. Vous devez choisir entrer le numéro de ligne. 1 est la ligne du haut, 2 la ligne du milieu et 3 la ligne du bas. Recommencez.") #row out of range
            
    # Ask player to choose a column
    column = ""
    
    # while column entry is out of range return error
    while column not in [1, 2, 3]:
        column = int(input(f"\nMaintenant choisissez une colonne entre 1 et 3 : ")) #column OK
    
        if column not in [1, 2, 3]:
            print("Entrée invalide. Vous devez choisir entrer le numéro de colonne. 1 est la colonne de gauche, 2 la colonne du milieu et 3 la colonne de droite. Recommencez.") #column out of range
    
    if assigned_symbol == symbol_1:
        board[row - 1][column - 1] = symbol_1
    else:
        board[row - 1][column - 1] = symbol_2
        
    # choice = actual_player[1]
    choice = [row, column, actual_player[1]]
    
    # Just for test => annotate before commit
    print(choice)
    