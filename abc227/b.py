from collections import Counter
n = int(input())
ss = dict(Counter(map(int, input().split())))
maxs = max(ss.keys())

ans = 0
for a in range(1, 1000):
    for b in range(1, 1000):
        s = 4 * a * b + 3 * a + 3 * b
        if s in ss:
            ans += ss[s]
            del ss[s]
        if s > maxs:
            break
print(n - ans)