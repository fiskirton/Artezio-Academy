"""
This module contains a generator function for
creating a dictionary from two lists
"""


def make_dict(keys, values):
    """
    Function generator to create a dictionary from lists.
    Returns the generator object.
    Keys without values are filled with the None value.
    Values without keys are ignored.
    """

    keys_iter = iter(keys)
    values_iter = iter(values)

    for _ in range(len(keys)):
        try:
            key = next(keys_iter)
            value = next(values_iter)
            yield key, value

        except StopIteration:
            yield key, None


if __name__ == '__main__':

    DICT_WITH_FILLER = dict(make_dict([1, 2], [1]))
    DICT_WITH_SLICE = dict(make_dict([1, 2], [1, 2, 3]))

    print(DICT_WITH_FILLER)
    print(DICT_WITH_SLICE)
