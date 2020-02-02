def f():
    return min(map(float,input().split()),key=abs)
print(f())
