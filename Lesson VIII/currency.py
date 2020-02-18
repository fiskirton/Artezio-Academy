"""
This module contains function to transfer currency
"""

import requests


def get_currency(value, source, target):
    """
    Convert the number of source currency to the
    target currency at the current rate
    """

    url = f'https://api.exchangerate-api.com/v4/latest/{source}'

    response = requests.get(url)

    try:
        response.raise_for_status()
        data = response.json()

    except requests.exceptions.HTTPError as request_er:
        return request_er

    try:
        target_currency = data['rates'][target.upper()] * value
        target_currency = float(f'{target_currency:.2f}')

    except KeyError:
        return "Target currency is not supported"

    return target_currency


if __name__ == '__main__':

    print(get_currency(100, 'rub', 'usd'))
    print(get_currency(100, 'usa', 'rub'))
    print(get_currency(100, 'usd', 'rus'))
