'''
In this Program you are given a String and two markers (the initial and final).
You have to find a substring ecnlosed between these two markers.
Conditions:
1. The initial and final markers are always diffrent
2. if there is no initial marker, then the first charackter should be considered the beginning of a string
3. if there is no final marker, then the last character should be considered the ending of a string
4. if the initial and final markers are missing then simply return the whole string
5. the final merker comes before the initial marker, then ruturn an empty string
'''


def between_two_markers(text: str, begin: str, end: str):




    # if initial and final marker are the same give back an empty string
    if begin == end:
        return " "

    # if the initial marker is in the text you search the text for this marker
    # and start from there. You have to add the length of the marker to get at the end of
    # the initial marker
    if begin in text:
        beginning = text.find(begin) + len(begin)

    # same procedure  with the end marker
    if end in text:
        ende = text.find(end)
    else:
        ende=len(text)


    return text[beginning:ende]



between_two_markers("Hallo wie geht es dir?", "Hallo", "?")
