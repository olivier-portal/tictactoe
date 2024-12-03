#Vérification de la case choisie
def checking_case(board):
    if board == " ":
        return True
    else:
        print("Case prise. Veuillez choisir une autre case")
        return False
# Autre option 
def checking_case(board):
    if board != " " or "X" or "O":
        print("Case prise. Veuillez choisir une autre case.")
        return False
    return True
# Autre option
def checking_case(board):
    if board == "X" or board == "O":
        print("Case prise. Veuillez choisir une autre case.")
        return True
    return False