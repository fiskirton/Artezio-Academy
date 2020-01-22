from random import randint

test_list = [randint(1, 10) for _ in range(10)]
print(test_list)

test_list = list(set(test_list))
print(test_list)