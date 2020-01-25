def range_impl(start=None, stop=None, step=1):

    if stop is None and start is not None:
        stop = start
        start = 0

    if stop is None and start is None:
        return

    if not step:
        return

    if start < stop and step < 0 or \
        start > stop and step > 0:
        return

    while True:
        if start >= stop and step > 0:
            break
        if start <= stop and step < 0:
            break

        yield start
        start += step

print(list(range_impl(10, 1, -2)))

for i in range_impl(1, 10):
    print(i)
