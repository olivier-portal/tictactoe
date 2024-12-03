from start_game_function import create_grid

board = create_grid()
choice = board[0][0]

# #Checking the chosen case
def checking_case(board, choice):
    if choice == " ":
        return True
    else:
         print("La case n'est pas vide. Veuillez choisir une autre case.")
         return False
    

