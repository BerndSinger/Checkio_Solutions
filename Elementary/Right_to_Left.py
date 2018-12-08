'''
In this program you get a sequence of strings as tuple of strings
You want to replace the word right with the worrd left
The program should also replace "right" when it is part of another word
Example= "rightfull" = "leftfull"
For this problem you can use string manipulation methods:
look up join() and replace() to get an idea how they work
'''

phrases=("right","left","righty", "stop")


def left_join(phrases):

    string1=(",".join(phrases))
    string1_left=string1.replace("right","left")

    return string1_left

print(left_join(phrases))
