def players_turn(actual_player, player1, player2):
# Define who starts first:
    if actual_player == player1:
        actual_player = player2
    else:
        actual_player = player1
  
    return actual_player
       