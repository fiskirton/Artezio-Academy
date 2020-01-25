from functools import reduce

def factorial(n):
    res = reduce(lambda x, ac: ac * x, range(1, n + 1))
    return res

print(factorial(5))