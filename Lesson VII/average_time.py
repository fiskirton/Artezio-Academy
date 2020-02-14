"""
This module contains decorator for measuring the average time
"""

import time
from collections import deque
from functools import wraps


def average_time(calls_num=1):
    """
    Decorator for measuring the average execution time of
    a function for the last n calls
    """

    def inner_decorator(func):

        queue = deque(maxlen=calls_num)

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal queue

            start = time.time()
            ret_val = func(*args, **kwargs)
            elapsed = time.time() - start

            queue.append(elapsed)
            average = int(sum(queue) // len(queue) * 1000)
            print(f'Average time: {average}ms')

            return ret_val

        return wrapper

    return inner_decorator


@average_time(calls_num=2)
def test(test_param):
    """
    func for testing average_time decorator
    """

    time.sleep(test_param)
    return test_param


if __name__ == '__main__':
    print(test(3))
    print(test(7))
    print(test(1))
