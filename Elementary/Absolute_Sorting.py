'''
This program sorts its elements  according to its absolute values
the method sorted() needs a so called "key" which specifies how the list is sorted
In this case its the method abs()
'''
numbers_array = [1, 5, -2, -32, 45, 0 ]

def sorted_absolute(numbers_array):

    numbers_array_sorted = sorted(numbers_array,key= abs)

    return numbers_array_sorted

print(sorted_absolute(numbers_array))
