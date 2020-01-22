def isbst(sets):
    a, b, c = sets
    return c <= a and c <= b

sets_input1 = [set([1,2]), set([2,3]), set([2])]
sets_input2 = [set([1,2]), set([3,4]), set([5])]

print(isbst(sets_input1))
print(isbst(sets_input2))
