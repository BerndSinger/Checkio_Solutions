'''
In this program you are given a string and there is a secret message hidden in it
Your program should extract all the upper case letters and then you will get the
secret message
method to use: string.isupper()
'''

string1="How are you? Eh, ok. Low or Lower? Ohhh."


def get_message(string1: str):
    result_message=""
    for letter in string1:
        if letter.isupper():
            result_message += letter

    return result_message

print(get_message(string1))
