import math

def sqrs(x):
    ods = filter(lambda el: bool(el & 1), range(0, x))
    ods_sqrs = list(map(lambda x: x * x, ods))
    print(ods_sqrs, len(ods_sqrs))


sqrs(10)
