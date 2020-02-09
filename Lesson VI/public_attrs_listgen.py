"""
This module contains a list generator function
"""


def get_public_attrs(obj):
    """
    Returns list of public attributes of object
    """

    return [attr for attr in dir(obj) if not attr.startswith('_')]


print(get_public_attrs(list))
