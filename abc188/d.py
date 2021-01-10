from collections import defaultdict

n, C = map(int, input().split())
data = [None] * n
for i in range(n):
    data[i] = tuple(map(int, input().split()))
data = sorted(data, key=lambda x: x[1])

period = defaultdict(int)
for i in range(n):
    period[data[i][0]] += data[i][2]
    period[data[i][1] + 1] -= data[i][2]
period = sorted(period.items())

cost = defaultdict(int)
c = 0
for p in period:
    c += p[1]
    cost[p[0]] = c
cost = sorted(cost.items())

c = 0
for i in range(len(cost) - 1):
    d = cost[i + 1][0] - cost[i][0]
    c += d * min(C, cost[i][1])
print(c)