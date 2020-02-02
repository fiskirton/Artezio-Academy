"""
This module contains function for working with http response
"""

import requests

import website_alive


def check_url_availability(url):
    """
    Returns response status code
    """

    response = website_alive.get_response_object(url)
    return response.status_code == requests.codes['ok']
