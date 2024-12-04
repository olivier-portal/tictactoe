def is_winner(board):
    winner_combinations = [
        board[0],  # first horizontal line
        board[1],  # second horizontal line
        board[2],  # third horizontal line
        [board[0][0], board[1][0], board[2][0]],  # first vertical line
        [board[0][1], board[1][1], board[2][1]],  # second vertical line
        [board[0][2], board[1][2], board[2][2]],  # third vertical line
        [board[0][0], board[1][1], board[2][2]],  # diagonal descendent
        [board[2][0], board[1][1], board[0][2]]   # diagonal ascendent
    ]

    for combination in winner_combinations:
        if all(cell == 'X' for cell in combination):
            print(" X est le gagnant!")
            return True
        elif all(cell == 'O' for cell in combination):
            print("O est le gagnant")
            return True

    print("Nadie ha ganado todavía")
    return False
