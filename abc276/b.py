from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)
for i in range(1, n + 1):
    print(len(d[i]), *sorted(d[i]))