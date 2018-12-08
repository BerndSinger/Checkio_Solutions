'''
This program takes a Text as input (Str) and returns the letter which occurs the most in that text. If two letters
have the same value it returns the letter that comes in the alphabet first
'''
text= "sssssbbbb"
def most_frequent_letter(text:str):

# all letters in the text will changed in lower case
    text=text.lower()

# initializing a dictonary where the key will be the letter and the value will be the number of times
# it occurs in the string
    counter={}

# getting rig of all non alphabetic symbols and joining it to one long string
    text= ''.join([x for x in text if x.isalpha()])


# now we loop through the sting and each letter will be stored as a key
# if the letter is already a key its value will be increased by one
    for char in text:

        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

# Sort the dictonary by letters so that a is at first place
    counter= sorted(counter.items())


# getting the maximum of that now LIST not dictonary with the max function
    key = max(counter, key=lambda x: x[1])

    return key[0]



print(most_frequent_letter(text))