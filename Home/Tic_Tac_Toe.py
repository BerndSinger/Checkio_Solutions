'''
In this programm you check if there is a winner in a Tic Tac Toe game or if its a draw
'''

list=["OXO",
      "XOX",
      "OxO"]

def check_winner(list):

    row1 = []
    row2 = []
    row3 = []

    for element in list[0]:
        row1.append(element)

    for element2 in list[1]:
        row2.append(element2)

    for element3 in list[2]:
        row3.append(element3)


    if row1[0]==row1[1]==row1[2] and row1[0]!= "." :
        if row1[0]=="X":
            return "X wins"
        elif row1[0]=="O":
            return "O wins"

    elif row2[0]==row2[1]==row2[2] and row2[0]!= "." :
        if row2[0]=="X":
            return "X wins"
        elif row2[0]=="O":
            return "O wins"

    elif row3[0]==row3[1]==row3[2] and row3[0]!= "." :
        if row3[0]=="X":
            return "X wins"
        elif row3[0]=="O":
            return "O wins"

    elif row1[0]==row2[0]==row3[0] and row1[0]!= "." :
        if row1[0]=="X":
            return "X wins"
        elif row1[0]=="O":
            return"O wins"

    elif row1[1]==row2[1]==row3[1] and row1[1]!= "." :
        if row1[1]=="X":
            return "X wins"
        elif row1[1]=="O":
            return"O wins"

    elif row1[2]==row2[2]==row3[2] and row1[2]!= "." :
        if row1[2]=="X":
            return "X wins"
        elif row1[2]=="O":
            return "O wins"

    elif row1[0]==row2[1]==row3[2] and row1[0]!= "." :
        if row1[0]=="X":
            return"X wins"
        elif row1[0]=="O":
            return"O wins"

    elif row1[0]==row2[1]==row3[2] and row1[0]!= "." :
        if row1[0]=="X":
            return"X wins"
        elif row1[0]=="O":
            return"O wins"

    elif row3[0]==row2[1]==row1[2] and row3[0]!= "." :
        if row3[0]=="X":
            return"X wins"
        elif row3[0]=="O":
            return"O wins"

    else:
        return "Draw"


print(check_winner(list))
