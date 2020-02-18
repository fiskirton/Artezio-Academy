"""
Contains regular expression for matching iso date format:
YYYY-MM-DDThh:mm:ss±hh:mm
"""

import re


if __name__ == '__main__':

    PATTERN = re.compile((r'((?P<date>'
                          r'(?P<year>[12]\d{3})-'
                          r'(?P<month>0[1-9]|1[0-2])-'
                          r'(?P<day>0[1-9]|[12]\d|3[01]))'
                          r'T(?P<time>'
                          r'(?P<hours>[01][1-9]|2[0-3]):'
                          r'(?P<minutes>[0-5][0-9]):'
                          r'(?P<seconds>[0-5][0-9])'
                          r'(?P<timezone>'
                          r'(?:-(?:0[1-9]|1[0-2])|\+(?:0[0-9]|1[0-4])):'
                          r'(?:00|30|45))))'))


    DATE = '2000-12-08T23:23:31+14:00'

    MATCH = re.match(PATTERN, DATE)
    print(MATCH.groups())
