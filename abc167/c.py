import itertools

n, m, x = map(int, input().split())
c = [None] * n
a = [None] * n
for i in range(n):
    aa = list(map(int, input().split()))
    c[i] = aa[0]
    a[i] = aa[1:]

ans = 100000000000
for k in range(1, n + 1):
    for cmb in itertools.combinations(range(n), k):
        d = [0] * m
        cost = 0
        for cm in cmb:
            cost += c[cm]
            for i in range(m):
                d[i] += a[cm][i]

        f = True
        for i in range(m):
            if d[i] < x:
                f = False
                break
        if f:
            ans = min(ans, cost)

if ans == 100000000000:
    ans = -1
print(ans)
