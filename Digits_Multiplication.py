'''
In this program you are given a positive integer. Your function should calculate the
product of the digits excluding any Zeros

First i transform the integer into a string so i can use a for loop over it
I check for every element if its a 0 and if not i will transform the string element
back into an integer and multiply it with my answer
'''



number=123405

def multiplication_of_numbers(number):

    answer=1

    string_number=str(number)

    for i in string_number:
        if int(i) == 0:
            answer=answer
        else:
            answer=answer*int(i)

    return answer

print(multiplication_of_numbers(number))