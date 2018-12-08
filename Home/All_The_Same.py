'''
In this program you check if all elements in the given list are
equal
To solve this problem there is a nice tool to use: sets
In sets there are just elements that are unique
So you use the set() method on the list and if all elements are equal it length will be
just 1 if its longer you know that there are elements in the list that are not unique
'''

data=[21,1]

def all_the_same2(data):

    if(len(set(data))==1) or len(data)<=1:
        return True
    return False

print(all_the_same2(data))

