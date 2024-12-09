# Create a tic tac toe game

# import functions
from functions.start_game import intro

from functions.define_players import define_players

from functions.define_symbol import define_symbol

from functions.create_grid import create_grid

from functions.print_board import print_board

from functions.choose_box import choose_box

from functions.checking_case import checking_case

from functions.fill_board import fill_board

from functions.is_winner import is_winner

from functions.is_board_full import is_board_full

from functions.players_turn import players_turn

"""
    The main() function stocks the principal functions in variables in order to call them at the end
    This function also allows you to keep in buffer the variables which will be used as arguments in another function 
    
    Example: The define-player() function defines the name of the 2 players, it returns the name of player 1 in the variable player1
             and the name of player 2 in the variable player2
             the player1 and player2 variables are stored and used as arguments in the symbol allocation function (X or O)
             => sym(player1, player2)
"""
def main():
    # Start the game
    intro() # Display Welcome message and remind the rules
    player1, player2 = define_players() # input players names
    symbol_1, symbol_2 = define_symbol(player1, player2) # Input symbols for each player (stock in players list)
    actual_player = player1 # Define who starts first
    board = create_grid() # Create the grid
    
    # Print the initial board (empty)
    print_the_board = print_board(board)
    
    # While the board is not full, continue to play
    while is_board_full(board): # While the game board isn't full it continues
        choice = choose_box(actual_player) # Permitt players to choose a box
        check = checking_case(board, choice) #Verify that the choosen box isn't allready chosen
        if check: # If the chosen box is emty do :
            fill_board(board, choice) # Fill the chosen box
            if is_winner(board, player1, player2) == False: # If there is no winner
                if is_board_full(board) == False: # If the board is full
                    print_board(board) # Print the full board
                    print("\nEgalité ! Bien joué à tous les deux.") # Send a message "this is a draw"
                    break # Stop the game
                else:
                    print_board(board) # If the board isn't full, print the board
                    actual_player = players_turn(actual_player, player1, player2) # Switch to the next player
            else:
                print_board(board) # If there is a winner, print board and send a message "player X wins"
                break 
        else:
            is_board_full(board) == True # If the board isn't full start again the loop for next move


main() #Launch the game