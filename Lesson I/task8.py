from collections import Counter
from random import randint

test_dict = {x: randint(1, 10) for x in range(10)}
print(test_dict)

counter = Counter(test_dict)
print(counter.most_common(3))