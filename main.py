# #Checking the chosen case
def checking_case(board, choice ):
    if choice == " ":
             return "ok"
    else:
         return "Case taken. Please choose another case."

board = [["X", " ", "X"],
        ["O", "O", "O"],
        ["O", " ", "X"]]

choice = board [2][2]
print(checking_case(board,choice))
