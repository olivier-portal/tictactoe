def choose_box(board, player1, player2, symbol_1, symbol_2):
    # Define who starts first:
    count = 1
    if count % 2 == 0:
        actual_player = player2[0]
    else:
        actual_player = player1[0]
    assigned_symbol = actual_player[1]
    print(f"\n{actual_player} c'est votre tour de jouer ! ")
    
    # Ask player to choose a row
    row = int(input(f"\nChoisissez une ligne entre 1 et 3 : "))
    column = int(input(f"\nMaintenant choisissez une colonne entre 1 et 3 : "))
    if assigned_symbol == symbol_1:
        board[row - 1][column - 1] = symbol_1
    else:
        board[row - 1][column - 1] = symbol_2
        
    choice = assigned_symbol
    
    return choice
    


    