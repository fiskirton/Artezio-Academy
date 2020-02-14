"""
This module contains currying decorator
"""

from functools import wraps, partial


def curry(func):
    """
    Currying decorator. Freezes passed arguments(using partial)
    until all arguments from the function signature will be received.
    Partial func also
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except TypeError:
            return partial(curry(func), *args, **kwargs)

    return wrapper


@curry
def foo(a, b, c, d, e):
    """
    Test func
    """
    return a + b + c + d + e


if __name__ == '__main__':
    f = foo(1)(2)(3)(4)(e=5)(f=6)
    print(f)
