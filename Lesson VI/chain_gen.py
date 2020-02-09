"""
This module contains functions for working with iterable objects
"""


def chain(*iterables):
    """
    A generator function that iterates over passed objects sequentially
    """

    for iterable in iterables:
        for item in iterable:
            yield item


if __name__ == '__main__':

    CHAIN = chain(['a', (1, 2), 3], {'b': 1}, (1.2, 0, 2.5),
                  {3, 4, 5}, map(str, [5, 6]))

    print(list(CHAIN))
