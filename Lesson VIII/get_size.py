"""
Simple module to try send get requests
"""

import requests


def get_page_size(url):
    """
    Sends get requests. Returns content size(symbols amount)
    """

    response = requests.get(url)
    return len(response.content)


if __name__ == '__main__':

    print(get_page_size('https://google.com'))
