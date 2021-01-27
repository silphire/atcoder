n, k= map(int, input().split())
r = [
    tuple(map(int, input().split()))
    for _ in range(k)
]
r = sorted(r)

x = [None] * n
x[0] = 1
for i in range(n):
    if x[i] is None:
        continue
    for j in range(k):
        f = False
        for p in range(r[j][0], r[j][1] + 1):
            if i + p >= n:
                f = True
                break
            if x[i + p] is None:
                x[i + p] = x[i]
            else:
                x[i + p] += x[i]
            x[i + p] %= 998244353
        if f:
            break
if x[n - 1] is None:
    print(0)
else:
    print(x[n - 1])