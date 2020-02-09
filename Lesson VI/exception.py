"""
Simple module for catching exceptions
"""


N = int(input())

for _ in range(N):
    try:
        a, b = map(int, input().split())
        print(a / b)

    except ZeroDivisionError as ex:
        print(f'Error Code: {ex}')

    except ValueError as ex:
        print(f'Error Code: {ex}')
