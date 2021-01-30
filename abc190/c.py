import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n, m = map(int, input().split())
a = [0] * m
b = [0] * m
for i in range(m):
    a[i], b[i] = map(int, input().split())
    a[i] -= 1
    b[i] -= 1

k = int(input())
c = [0] * k
d = [0] * k
for i in range(k):
    c[i], d[i] = map(int, input().split())
    c[i] -= 1
    d[i] -= 1

ans = 0
for i in range(2 ** k):
    dish = [0] * n
    for j in range(k):
        if i & (1 << j) == 0:
            dish[c[j]] = 1
        else:
            dish[d[j]] = 1
    x = 0
    for j in range(m):
        if dish[a[j]] == 1 and dish[b[j]] == 1:
            x += 1
    ans = max(ans, x)
print(ans)