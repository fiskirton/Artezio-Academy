"""
This module contains decorator for checking annotations
"""

from functools import wraps


def check_annotations(func):
    """
    Checks annotations of func arguments.
    If func has no annotations or has partial annotations, will raise
    TypeError.
    If annotation do not match, will print warning message.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) == len(func.__annotations__):
            for arg, annotation in zip(args, func.__annotations__.items()):
                if not isinstance(arg, annotation[1]):
                    message = f'Warning: {annotation[0]}={arg} \
should have type {annotation[1].__name__}'

                    print(message)
        else:
            raise TypeError("not all parameters are annotated")

        return func(*args, **kwargs)
    return wrapper


@check_annotations
def test_func(arg_1: int, arg_2: list, arg_3: float):
    """
    Test func
    """
    return arg_1, arg_2, arg_3


if __name__ == '__main__':
    print(test_func(1, [], 3))
