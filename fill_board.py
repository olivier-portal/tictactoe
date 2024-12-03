from start_game_function import print_board

# Define player's turn and fill a box with the predefined symbol
def fill_board(board, player1, player2, symbol_1, symbol_2, choice):
    choice = input(f"\n{player1} à vous de jouer, choisissez une case entre 1 et 9 : ")
    if choice == 1:
        choice = board[0][0]      
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
    
    return board, choice