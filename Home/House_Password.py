'''
This Programm checks if your Password contains atleast a diggit a uppercase letter and a lowercase letter. If all these #
conditions are met and it is longer than 10 your password is considered safe
'''

data='Aaaaaaaaaaaaaaa2'

def password_strength(data: str):
    '''
        Function that takes an string as input and returns a boolean
        if the variables flag_isUpper, flag_isLower, and flag_isDigit are all 1 it returns true, if not it returns false

    '''
    flag_isUpper=0
    flag_isLower=0
    flag_isDigit=0

    if len(data) < 10:
        return False
    for element in data:
        if element.isupper():
            flag_isUpper=1
            continue
        if element.isdigit():
            flag_isDigit=1
            continue
        if element.islower():
            flag_isLower=1
            continue

    if flag_isDigit==1 and flag_isLower==1 and flag_isUpper==1:
        return True
    else:
        return False


print(password_strength(data))
