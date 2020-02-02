"""
This module contains function for working with
multiple parameters
"""

from collections.abc import Iterable
from functools import reduce


def make_sum_and_product(*args, **kwargs):

    """
    This function converts the nested lists
    to a single one and returns
    the sum and product of nonzero elements.
    """

    def make_flat(collection, flat):
        #
        for item in collection:

            if isinstance(item, Iterable):
                if not any(i in item for i in item):
                    make_flat(item, flat)
                else:
                    flat.append(None)
            else:
                flat.append(item)

        return flat

    kwargs_tuple = tuple(kwargs.values())
    flat_args = make_flat(args + kwargs_tuple, [])

    if None in flat_args:
        print("Reference cycle have been found")
        return None

    coll_summ = sum(flat_args)
    coll_product = reduce(lambda ac, x: ac * x if x else ac, flat_args)

    return coll_summ, coll_product


# CYCLE = [1, 2]
# CYCLE.append(CYCLE)
# print(make_sum_and_product(1, 2, [3, 4, (5, 6, 0)], a=(10, 11, CYCLE),
#                            b=(3, 4, [5, 6, [7, 8], []])))
