import sys
sys.setrecursionlimit(10 ** 9)

n, x, y = map(int, input().split())

def red(lv, nr):
    global x, y
    if lv < 2:
        return 0
    return red(lv - 1, nr) + blue(lv, x * nr)

def blue(lv, nr):
    global x, y
    if lv == 1:
        return nr
    return red(lv - 1, nr) + blue(lv - 1, y * nr)

print(red(n, 1))