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

    print("C'est un match nul !")
    return False

# This is the first version, with redundances but simple to know how find a solution
'''def is_winner(board):
    win_checker = False

    while win_checker == False:
        if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
            print("X ha ganado con 1ra línea horizontal")
            win_checker = True
        elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
            print("X ha ganado con 2da línea horizontal")
            win_checker = True
        elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
            print("X ha ganado con 3ra línea horizontal")
            win_checker = True
        elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
            print("X ha ganado con 1ra línea vertical")
            win_checker = True
        elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
            print("X ha ganado con 2da línea vertical")
            win_checker = True
        elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
            print("X ha ganado con 3ra línea vertical")
            win_checker = True
        elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
            print("X ha ganado con la diagonal descendiente")
            win_checker = True
        elif board[2][0] == "X" and board[1][1] == "X" and board[0][2] == "X":
            print("X ha ganado con la diagonal cresciente")
            win_checker = True
        else:
            win_checker = False
            break


    while win_checker == False:
        if board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
            print("O ha ganado con 1ra línea horizontal")
            win_checker = True
        elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
            print("O ha ganado con 2da línea horizontal")
            win_checker = True
        elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
            print("O ha ganado con 3ra línea horizontal")
            win_checker = True
        elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
            print("O ha ganado con 1ra línea vertical")
            win_checker = True
        elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
            print("O ha ganado con 2da línea vertical")
            win_checker = True
        elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
            print("O ha ganado con 3ra línea vertical")
            win_checker = True
        elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
            print("O ha ganado con la diagonal descendiente")
            win_checker = True
        elif board[2][0] == "O" and board[1][1] == "O" and board[0][2] == "O":
            print("O ha ganado con la diagonal cresciente")
            win_checker = True
        else:
            win_checker = False
            break

    if win_checker:
        print("YOU'RE THE WINNER!")

board = [["X", "O", "X"],
        ["O", "X", "O"],
        ["O", "X", "O"]]

is_winner(board)
'''