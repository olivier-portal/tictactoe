def choose_box(actual_player):
    # Define who starts first:

    print(f"\n{actual_player[0]} c'est votre tour de jouer ! ")
    
    # Ask player to choose a row
    row = ""
    
    # While row entry is out of range return error
    while row not in [1, 2, 3]:
        try:
            row = int(input(f"\nChoisissez une ligne entre 1 et 3 : ")) #row OK
        
            if row not in [1, 2, 3]:
                print("Le chiffre doit être 1, 2 ou 3. Vous devez choisir le numéro de ligne: 1 est la ligne du haut, 2 la ligne du milieu et 3 la ligne du bas. Recommencez.") #row out of range
        except ValueError:
            print("Ce n'est pas un nombre. Vous devez choisir le numéro de colonne. 1 est la colonne de gauche, 2 la colonne du milieu et 3 la colonne de droite. Recommencez.") #If player enter anything but a number
        
            
    # Ask player to choose a column
    column = ""
    
    # while column entry is out of range return error
    while column not in [1, 2, 3]:
        try:
            column = int(input(f"\nMaintenant choisissez une colonne entre 1 et 3 : ")) #column OK
        
            if column not in [1, 2, 3]:
                print("Le chiffre doit être 1, 2 ou 3. Vous devez choisir le numéro de ligne: 1 est la ligne du haut, 2 la ligne du milieu et 3 la ligne du bas. Recommencez.") #row out of range
        except ValueError:
            print("Ce n'est pas un nombre. Vous devez choisir le numéro de colonne. 1 est la colonne de gauche, 2 la colonne du milieu et 3 la colonne de droite. Recommencez.") #If player enter anything but a number
    
    choice = [row, column, actual_player[1]]
    
    return choice
    