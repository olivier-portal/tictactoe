def is_winner(board, player1, player2):
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
        if all(cell == player1[1] for cell in combination):
            print(f" {player1[0]} est le gagnant!")
            return True
        elif all(cell == player2[1] for cell in combination):
            print(f"{player2[0]} est le gagnant")
            return True

    return False
