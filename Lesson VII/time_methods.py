"""
This module contains decorator for mesuring of execution time
"""

import time
from collections.abc import Callable
from functools import wraps


def measure_time(func):
    """
    Decorator for mesuring of execution time
    """

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.time()
        result = func(*args, **kwargs)
        elapsed = float(f'{time.time() - start:.3f}')
        print(f'"{func.__name__}" execution time: {elapsed}sec')

        return result
    return wrapper


def time_methods(decorator, *args):
    """
    Decorator for wrapping methods of class a_class,
    whose names are passed to args, by another decorator
    """

    def class_decorator(a_class):
        for attr in args:
            if hasattr(a_class, attr):
                class_member = getattr(a_class, attr)
                if isinstance(class_member, Callable):
                    setattr(a_class, attr, decorator(class_member))

        return a_class
    return class_decorator


@time_methods(measure_time, 'inspect', 'get_test_param', 'finilize')
class Spam:
    """
    Test class
    """

    def __init__(self, test_param):
        self.test_param = test_param

    def inspect(self):
        """
        Test method
        """

        time.sleep(self.test_param)

    def get_test_param(self):
        """
        Test method
        """

        return self.test_param


if __name__ == '__main__':
    TEST_OBJ = Spam(1)
    TEST_OBJ.inspect()
    RES = TEST_OBJ.get_test_param()
    print(RES)
    print(TEST_OBJ.inspect.__name__)
