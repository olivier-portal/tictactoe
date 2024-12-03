def choose_box(board, player1, player2, symbol_1, symbol_2):
    # Define who starts first:
    # if count % 2 == 0:
    #     actual_player = player2
    # else:
    actual_player = player1
    # print(f"\n{actual_player} c'est votre tour de jouer ! ")
    # define rows and cols
    rows = [1, 2, 3]
    columns = [1, 2, 3]
    
    # Ask player to choose a row
    row = int(input(f"\n{actual_player} choisissez une ligne entre 1 et 3 : "))
    column = int(input(f"\nMaintenant choisissez une colonne entre 1 et 3 : "))
    if actual_player == symbol_1:
        board[row][column] = symbol_1
    else:
        board[row][column] = symbol_2
    return board


    