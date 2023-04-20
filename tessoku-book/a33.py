import functools
input()
if functools.reduce(lambda x, y: x ^ y, map(int, input().split())) != 0:
    print('First')
else:
    print('Second')