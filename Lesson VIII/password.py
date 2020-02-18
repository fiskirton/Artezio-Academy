"""
Contains regular expression for detecting password
"""

import re


if __name__ == '__main__':

    PATTERN = re.compile((
        r'^(?=.*[a-z])'  # at least one lowercase letter
        r'(?=.*[A-Z])'  # at least one capital letter
        r'(?=.*\d)'  # at least one digit
        r'[\w\d\*%&_]{8,12}$'  # available spec symbols, length range
    ))

    PASSWORD = 'Aa89_%*&'

    MATCH = re.match(PATTERN, PASSWORD)

    print(MATCH)
