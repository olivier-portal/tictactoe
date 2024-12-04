def players_turn(actual_player, player1, player2):
# Define who starts first:
    if actual_player is player1:
        actual_player = player2
    else:
        actual_player = player1
    print(f"\n{actual_player[0]} c'est votre tour de jouer ! ")
 
  
    return actual_player