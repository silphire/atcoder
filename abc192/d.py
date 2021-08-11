import sys

sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7
input = sys.stdin.readline

x = input().rstrip()
m = int(input())

d = max(map(int, list(x)))

if len(x) == 1:
    print(int(int(x) <= m))
    exit()

def f(rad):
    global x
    global m

    a = 0
    for c in x:
        a = a * rad + int(c)
        if a > m:
            return float('inf')
    return a

if f(d) > m:
    print(0)
    exit()

ans = 0
l = d + 1
r = 10 ** 18
while r - l > 0:
    dd = (l + r) // 2
    if f(dd) > m:
        r = dd - 1
    else:
        l = dd + 1

l -= 10
l = max(1, l)
for a in range(l, l + 100):
    if f(a) > m:
        print(a - d - 1)
        exit()