from create_grid import create_grid

# board = create_grid()
# choice = [0, 1, "O"]
# board = [[' ', ' ', 'O'], [' ', ' ', ' '], [' ', ' ', ' ']]

# #Checking the chosen case
def checking_case(board, choice):
    row = choice[0]
    column = choice[1]
    if board[row - 1][column - 1] == " ":
        return True
    else:
         print("\nLa case n'est pas vide. Veuillez choisir une autre case.")
         return False
     
        
