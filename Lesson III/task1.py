"""
This module contains some functions
for working with collections.
"""


def get_sqrs(collection):
    """Returns a list with squares of collection items."""
    return [x * x for x in collection]


def get_even_positions(collection):
    """Returns list of items at even collection positions."""
    return collection[::2]


def get_even_cubes_ods_position(collection):
    """
    Returns list with cubes of even elements
    at odd collection positions.
    """
    filtered_elements = list(filter(lambda x: not x % 2, collection[1::2]))
    result_collection = list(map(lambda x: x ** 3, filtered_elements))
    return result_collection


# COLL = list(range(1, 10))

# print(get_sqrs(COLL))
# print(get_even_positions(COLL))
# print(get_even_cubes_ods_position(COLL))
