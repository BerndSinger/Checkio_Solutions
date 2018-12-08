'''
You are given an array of numbers, You should find the difference between the maximum and
minimum element.
Your function should handle an undefined amount of arguments
'''

def difference_between_numbers(*args):
    if not args:
        return 0
    else:
        maximum = max(args)
        minimum = min(args)
        print(maximum)
        print(minimum)
        difference = maximum - minimum

        return difference

