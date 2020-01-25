def find_between(a, b, c):
    numbers_between = list(filter(lambda x: not x % c, range(a, b)))
    print(numbers_between, len(numbers_between))

find_between(1, 29, 6)
