'''
You are given a set of square coordinates where we have placed white pawns
You should count how many pawns are safe
'''

pawns={"b4", "d4", "f4", "c3", "e3", "g5", "d2"}


def pawns_safe(pawns):
    pawns_indexes=set()
    for elements in pawns:
        row=int(elements[1])-1
        col=ord(elements[0])-97
        pawns_indexes.add((row,col))

    # printed that out for better understanding how the tuples are ordered
    # draw that into a chess grid and you can see which pawns are safe
    print(pawns_indexes)
    count =0
    # here you check if the pawns are safe
    # pawns are safe if they stand diagonal towards each other
    # so you check your pawn_indexes if they have a pawn that is in the row below and
    # is just one column away in both sides
    for row,col in pawns_indexes:
        is_safe=((row - 1, col - 1) in pawns_indexes) or ((row - 1, col + 1) in pawns_indexes)
        if is_safe:
            count=count+1

    return count

print(pawns_safe(pawns))
