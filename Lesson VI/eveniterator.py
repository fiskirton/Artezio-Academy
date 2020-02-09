"""
Module contains a simple iterator
"""


class EvenIterator:
    """
    Sequence iterator. Returns elements at even positions
    """

    def __init__(self, iterable):

        self.seq = iter(iterable)

    def __next__(self):

        num = next(self.seq)

        if num:
            next(self.seq)
        else:
            raise StopIteration

        return num

    def __iter__(self):
        return self


if __name__ == '__main__':

    EVEN_ITER = EvenIterator([1, 2, 3, 4, 5, 6])

    for i in EVEN_ITER:
        print(i)
