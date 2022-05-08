n, q = map(int, input().split())

aa = [i + 1 for i in range(n)]
rr = {(i + 1):i for i in range(n)}
xx = [int(input()) for _ in range(q)]

for x in xx:
    p = rr[x]
    q = p + 1
    if q == n:
        q = n - 2
    y = aa[q]
    aa[p], aa[q] = aa[q], aa[p]
    rr[x] = q
    rr[y] = p
print(*aa)