from collections import Counter

n, k = map(int, input().split())
aa = list(map(int, input().split()))

tb = [0] * (n + 1)
for v, c in sorted(Counter(aa).items()):
    if v > 0:
        tb[v] = min(tb[v - 1], c, k)
    else:
        tb[v] = min(c, k)

ans = 0
for i in range(1, n + 1):
    d = tb[i - 1] - tb[i]
    ans += i * d
print(ans)