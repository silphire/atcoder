from collections import Counter

n = int(input())
aa = list(map(int, input().split()))

sa = [0] * (n + 1)
for i, a in enumerate(aa):
    sa[i + 1] = sa[i] + a

ans = 0
ctr = Counter(sa)
for v in ctr.values():
    ans += v * (v - 1) // 2
print(ans)