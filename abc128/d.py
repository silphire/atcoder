n, k = map(int, input().split())
vv = list(map(int, input().split()))

maxans = 0
for i in range(n + 1):
    for j in range(n + 1):
        if i + j > min(n, k):
            continue
        s = sorted(vv[:i] + vv[n-j:])
        ans = sum(s)
        r = k - i - j
        if r > 0:
            ns = min(len(s), r)
            for p in range(ns):
                if s[p] >= 0:
                    break
                ans -= s[p]
        maxans = max(maxans, ans)
print(maxans)