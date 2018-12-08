'''
In this programm the Hamming distance between two integers is calculated
You need to transform the 2 integers you are given into binary code
'''

number1 = 1
number2 = 999999

# transforming into binary code

def binary_code(number1, number2):

    binary_number1 = '{0:08b}'.format(number1)
    binary_number2 = '{0:08b}'.format(number2)
    counter=0

    # getting the two binarys into the same format length
    for element in binary_number1:
        if len(binary_number1)> len(binary_number2):
            binary_number2="0" + binary_number2

    for element in binary_number2:
        if len(binary_number2)> len(binary_number1):
            binary_number1="0" + binary_number1

    # comparing the two binary for each element
    # and increase the counter if they are not the same

    for element1, element2 in zip(binary_number1,binary_number2):
        if element1 != element2:
            counter= counter +1

    return counter



print(binary_code(number1,number2))
