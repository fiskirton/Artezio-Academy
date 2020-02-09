"""
This module contains function generator, which makes a cycled iterator
from iterable sequence
"""


def cycle(sequence):
    """
    Infinite cycle of iterations of sequence
    """

    while sequence:
        for item in sequence:
            yield item


if __name__ == '__main__':

    CYCLE = cycle([1, 2, 3])

    for i in range(10):
        print(next(CYCLE))
