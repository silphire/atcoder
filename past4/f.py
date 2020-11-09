from collections import Counter

n, k = map(int, input().split())

c = Counter([input() for _ in range(n)])
ra = Counter(c.values())
c = sorted(c.items(), key=lambda x: -x[1])
ans = c[k - 1]
if ra[ans[1]] > 1:
    print('AMBIGUOUS')
else:
    print(ans[0])