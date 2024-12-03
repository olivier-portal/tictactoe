def is_board_full(board):
    i=0
    while i < len(board):       # Un bucle que recorre el "board"
        dispo = " " in board[i] # Evalúa si un espacio vacío " " se encuentra en la lista con índice que cambia en cada bucle,
                                # si NO lo encuentra devuelve "False"
                                # si lo encuentra devuelve "True"
        i += 1
        if dispo:               # Si dispo es "True"
            break               # El bucle se detiene
    return dispo                # La función arroja:

board = [
    ["X", "O", "X"],
    ["X", "X", "O"],
    ["O", "X", "X"]
]

print(is_board_full(board))