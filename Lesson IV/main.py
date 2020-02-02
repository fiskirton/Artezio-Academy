"""
This module launches programm
"""

import website_alive


if __name__ == '__main__':
    URL = input()
    print('Resource availability: ', website_alive.check_url_availability(URL))
