import bisect

n = int(input())
ss = [input() for _ in range(n)]
tt = sorted(ss)

for i, s in enumerate(ss):
    j = bisect.bisect_left(tt, s)
    ans = 0
    if j > 0:
        for k in range(min(len(s), len(tt[j - 1]))):
            if s[k] != tt[j - 1][k]:
                break
            ans = max(ans, k + 1)
    if j < n - 1:
        for k in range(min(len(s), len(tt[j + 1]))):
            if s[k] != tt[j + 1][k]:
                break
            ans = max(ans, k + 1)
    print(ans)