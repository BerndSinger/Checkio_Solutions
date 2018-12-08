'''
this programm detects the longest substring in a string
and gives out his length as an integer
'''

line=""

if line==[]:
    print("0")
else:
    counter_list=[len(line)]
print(counter_list)
counter = 0

# list that contains all the counters of the substring


# loop over the length of the string

for i in range(len(line)):
    # checking if the current substring is the same as the substring before if true counter goes up by one
    if line[i]== line[i-1]:
        counter=counter+1
        # creating a list of the counters
        counter_list.append(counter)
    # if substring is not the same as before counter set back to one because we are now inside the string
    else:
        counter = 1
if counter_list==[]:
    print("0")
else:
    print(max(counter_list))

# def long_repeat(line):
#     count = 0
#     current_len = 1
#     for i in range(len(line)-1):
#         char = line[i]
#         next_char = line[i + 1]
#         if char == next_char:
#             current_len += 1
#         else:
#             if current_len > count:
#                 count = current_len
#             current_len = 1
#         if current_len > count:
#             count = current_len
#     return count
#
# print(long_repeat(line))