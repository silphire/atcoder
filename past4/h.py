from collections import Counter

n, m, k = map(int, input().split())
s = [
    list(input().rstrip())
    for _ in range(n)
]

maxn = 0
for yy in range(n):
    for xx in range(m):
        c = Counter()
        for i in range(min(m - xx, n - yy)):
            c[s[yy + i][xx + i]] += 1
            for y in range(i):
                c[s[yy + y][xx + i]] += 1
            for x in range(i):
                c[s[yy + i][xx + x]] += 1
            if c.most_common(1)[0][1] + k >= (i + 1) ** 2:
                maxn = max(maxn, i + 1)
print(maxn)