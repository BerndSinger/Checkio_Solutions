
'''
In this program you are given an array with positive numbers and a number N.
You should find the N-th power of the element in the array with the index N.
If N is outside of the array then return -1
Remember: first element has the index 0
'''


array = [1, 2, 3, 4]

def index_power(array,n):
    '''

    :param array: list of intergers
    :param n: power of the element
    :return: n-th power of the choosen element
    '''
    if len(array) >= n:
        return -1
    else:
        return array[n]**n


print(index_power(array,3))
