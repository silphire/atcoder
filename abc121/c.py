n, m = map(int, input().split())
cost = [None] * n
for i in range(n):
    cost[i] = tuple(map(int, input().split()))
cost = sorted(cost)
x = 0
for a, b in cost:
    if m <= 0:
        break
    x += a * min(b, m)
    m -= b
print(x)
