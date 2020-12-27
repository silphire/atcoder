n, m = map(int, input().split())
a = [None] * n
b = [None] * n
c = [None] * m
d = [None] * m

for i in range(n):
    a[i], b[i] = map(int, input().split())
for i in range(m):
    c[i], d[i] = map(int, input().split())

for i in range(n):
    md = 10 ** 9
    mj = 0
    for j in range(m):
        ds = abs(a[i] - c[j]) + abs(b[i] - d[j])
        if ds < md:
            md = ds
            mj = j
    print(mj + 1)
