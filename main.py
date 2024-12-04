# Create a tic tac toe game

# import functions
from start_game import intro

from define_players import define_players

from define_symbol import define_symbol

from create_grid import create_grid

from print_board import print_board

from choose_box import choose_box

from checking_case import checking_case

from fill_board import fill_board

from is_winner import is_winner

from is_board_full import is_board_full

from players_turn import players_turn

"""
    The main() function stocks the principal functions in variables in order to call them at the end
    This function also allows you to keep in buffer the variables which will be used as arguments in another function 
    
    Example: The define-player() function defines the name of the 2 players, it returns the name of player 1 in the variable player1
             and the name of player 2 in the variable player2
             the player1 and player2 variables are stored and used as arguments in the symbol allocation function (X or O)
             => sym(player1, player2)
"""
def main():
    introduction = intro()
    player1, player2 = define_players()
    symbol_1, symbol_2 = define_symbol(player1, player2)
    actual_player = player1
    board = create_grid()
    print_the_board = print_board(board)
    while is_board_full(board) == True:
        choice = choose_box(actual_player, player1, player2)
        check = checking_case(board, choice)
        if check:
            fill_board(board, choice)
            if is_winner(board, player1, player2) == False:
                if is_board_full(board) == False:
                    print("Egalité")
                    break
                else:
                    print_board(board)
                    players_turn(actual_player, player1, player2)
            else:
                break 
        else:
            choice = choose_box(player1,player2)


main()