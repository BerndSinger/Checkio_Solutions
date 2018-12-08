'''
In this program you check if a string contains three words in succession.
Example: "start 5 one two three 6 end" contains three words in succssion
Methods to use:
string.split()
string.isalpha()
'''
str1= "He is 123 man "
new_str1= str1.split()
print(new_str1)

def hello(new_str1):

    counter_words=0
    for i in new_str1:
        if i.isalpha():
            counter_words=counter_words+1
            if counter_words >= 3:
                return True
                break
        else:
            counter_words=0

    return False
