
'''
In this program you determine the popularity of certain words in a text
At the input of your function are given 2 arguments:
The text and the array of words the popularity of you need to determine
Following Conditions should be met:
1. The words schould be sought out in all registers. This means that if you need
to find a word "one" then words like "One", "ONE", "OnE" will do
2.the search words are always indicated in the lowercase
3. the word wasnÄt found even once, it has to be returned in the dictonary with zero vlaue
'''

test_string ='''When I was One
I had just begun
When I was Two
I was nearly new'''

words= ["i","was","three","near"]

def find_word(test_string,words):
    # initiliazing an empty dictonary
    answer = {}

    # converting all characters into lower case characters
    test_string=test_string.lower()
    # split the string into a list with every word as an element
    splitted_words= test_string.strip()

    # now you iterate over the given words you want to count
    for  word in words:
        answer[word]=splitted_words.count(word)

    return answer

print(find_word(test_string,words))


