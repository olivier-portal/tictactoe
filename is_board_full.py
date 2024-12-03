def is_board_full(board):
    i=0
    while i < len(board):       # A loop through the “board”
        dispo = " " in board[i] # Evaluates whether an empty space “ ” 
                                # is found in the list with index that changes in each loop,
                                # if NOT found it returns “False”.
                                # if found, it returns “True”.
        i += 1
        if dispo:               # Si dispo is "True"
            break               # Loop stops
    return dispo                # The function returns a Boolean value

board = [
    ["X", "O", "X"],
    ["X", "X", "O"],
    ["O", "X", "X"]
]

print(is_board_full(board))