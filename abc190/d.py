import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n = int(input())

udiv = []
ldiv = []
x = 1
while x * x <= n:
    if n % x == 0:
        ldiv.append(x)
        if x != n // x:
            udiv.append(n // x)
    x += 1
div = ldiv + udiv[::-1]
del ldiv
del udiv

ans = 0
for x in div:
    y = n // x
    if x % 2 == 1:
        ans += 1
print(ans * 2)