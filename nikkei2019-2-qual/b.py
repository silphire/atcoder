from collections import Counter

n = int(input())
dd = list(map(int, input().split()))

ctr = Counter(dd)
if dd[0] == 0 and ctr[0] == 1:
    ans = 1
    for i in range(1, max(dd) + 1):
        ans *= ctr[i - 1] ** ctr[i]
        ans %= 998244353
    print(ans)
else:
    print(0)
