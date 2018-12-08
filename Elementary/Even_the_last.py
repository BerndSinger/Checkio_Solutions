'''
In this program you are given an array of integers.
You schould find the sum of the integers with even indexes and
then multiply this summed number and the final element of the array together
Here you learn how to index through an array:
'''



array = [0, 1, 2, 3, 4, 5]

def even_the_last(array):

    last_element = array[-1]
    # the two ":" mean that you index through to whole array but the "2" means
    # you just take every second element and save it to a new array
    even_elements = array[::2]

    sum_even_elements = sum(even_elements)

    answer = sum_even_elements*last_element

    return answer

print(even_the_last(array))
