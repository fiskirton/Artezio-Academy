"""
This module contains function for working with http response
"""

import requests


def get_response_object(url):
    """
    Returns response object
    """

    return requests.get(url)
