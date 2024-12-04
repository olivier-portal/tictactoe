#Attribute a symbol to each player
def define_symbol(player1, player2):
    # ---------------------------------------------------------------------
    # player1 choose a symbol, the other symbol is automatically attributed to player2
    symbol_1 = ""
    while symbol_1 not in ["O", "X"]:  # Loop until valid input is given
        
        symbol_1 = input(f"\n{player1[0]}, voulez-vous jouer avec les O ou les X ? ").upper()
        #player1 chooses a symbol and uppercase / lowercase are handeled
        
        if symbol_1 not in ["O", "X"]:
            print("Entrée invalide. Vous devez choisir entre 'O' et 'X'. Recommencez.")
        # if char is out of range => return error message + start the loop again

    # player1 chooses a symbol and it assigns automatically the left symbol to player2
    if symbol_1 == "O":
        player1[1] = "O"
        player2[1] = "X"
        
    else:
        player2[1] = "O"
        player1[1] = "X"        
    
    print(f"\n{player1[0]}, vous jouez avec les {player1[1]} !")
    print(f"{player2[0]}, vous jouez avec les {player2[1]} !\n")

    return player1[1], player2[1]