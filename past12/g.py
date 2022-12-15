from collections import Counter

n, l, k = map(int, input().split())
ss = [
    input().rstrip()
    for _ in range(n)
]

ans = 0
for i in range(2 ** l):
    d = []
    cnt = 0
    j = 0
    a = i
    while a > 0:
        if a & 1 == 1:
            cnt += 1
            d.append(j)
        j += 1
        a >>= 1
    if cnt != k:
        continue

    xx = [None] * n
    for j in range(n):
        s = list(ss[j])
        for p in d:
            s[p] = '?'
        xx[j] = ''.join(s)
    ans = max(ans, Counter(xx).most_common()[0][1])
print(ans)