from collections import defaultdict

n = int(input())
r = defaultdict(int)
for _ in range(n):
    a, b = map(int, input().split())
    r[a] += 1
    r[a + b] -= 1
r = sorted(r.items(), key=lambda x: x[0])

s = []
for d, c in r:
    if s:
        s.append((d, s[-1][1] + c))
    else:
        s.append((d, c))

d = defaultdict(int)
for i in range(len(s) - 1):
    days = s[i + 1][0] - s[i][0]
    k = s[i][1]
    d[k] += days

print(' '.join(map(str, [d[i + 1] for i in range(n)])))
