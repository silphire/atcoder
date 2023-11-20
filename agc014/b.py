from collections import defaultdict
n, m = map(int, input().split())
d = defaultdict(int)
for _ in range(m):
    a, b = map(int, input().split())
    d[a] += 1
    d[b] += 1
for x in d.values():
    if x % 2 != 0:
        print('NO')
        exit()
print('YES')