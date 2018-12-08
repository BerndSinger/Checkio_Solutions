'''
THis programm takes a list as input and gives back a list of all
not unique elements of the first list
'''

data = [1,2,5,4,3,2,3,4]

def unique_elements(data):
    data2=[]
    for element in data:
        # data.count() counts how many times a element occurs in a list
        if data.count(element)>1:
            data2.append(element)

    return data2

# second way of solving the problem using "list comprehension"
def unique_elements_list_comprehension(data):

    return [val for val in data if data.count(val) > 1]


print(unique_elements(data))
print(unique_elements_list_comprehension(data))
