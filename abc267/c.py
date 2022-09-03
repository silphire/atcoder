n, m = map(int, input().split())
aa = list(map(int, input().split()))

bb = [0] * (n - m + 1)
for i in range(m):
    bb[0] += aa[i]
for i in range(1, n - m + 1):
    bb[i] = bb[i - 1] - aa[i - 1] + aa[i - 1 + m]

cc = [0] * (n - m + 1)
for i in range(m):
    cc[0] += (i + 1) * aa[i]
ans = cc[0]
for i in range(1, n - m + 1):
    cc[i] = cc[i - 1] - bb[i - 1] + aa[i - 1 + m] * m
    ans = max(ans, cc[i])
print(ans)