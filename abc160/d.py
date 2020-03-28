from collections import defaultdict

n, x, y = map(int, input().split())
x -= 1
y -= 1

ctr = defaultdict(int)

for i in range(n):
    for j in range(i + 1, n):
        v = min(j - i, abs(x - i) + 1 + abs(j - y))
        ctr[v] += 1

for i in range(1, n):
    print(ctr[i])