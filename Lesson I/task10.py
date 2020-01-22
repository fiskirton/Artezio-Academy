from random import randint

test_list1 = [randint(1, 10) for _ in range(10)]
test_list2 = [randint(1, 10) for _ in range(10)]
print(test_list1, test_list2)

result = list(set(test_list1) ^ set(test_list2))
print(result)