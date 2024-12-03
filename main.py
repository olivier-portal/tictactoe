from start_game_function import intro, define_players, define_symbol, create_grid, print_board

from choose_box import choose_box

from checking_case import checking_case

from fill_board import fill_board

from is_winner import is_winner

# from is_board_full import is_board_full

# Create a tic tac toe game

def main():
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
    print_the_board = print_board(board)
    choice = choose_box(board, player1, player2, symbol_1, symbol_2)
# start_game()

# choose_box()

# checking_case(create_grid, choice)

# if checking_case:
#     fill_board(board, choice)

main()