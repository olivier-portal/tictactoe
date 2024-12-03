###################

'''dispo = " " in board[0]
print(dispo)

dispo = " " in board[1]
print(dispo)

dispo = " " in board[2]
print(dispo)'''
def is_board_full(board):
    i=0
    while i < len(board):
        dispo = " " in board[i]
        #print(dispo)
        i += 1
        if dispo:
            print("Hay espacio disponible")
            break
    return dispo

board = [
    ["X", "O", "X"],
    ["X", "X", "O"],
    ["O", " ", "X"]
]

print(is_board_full(board))