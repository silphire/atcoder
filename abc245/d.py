n, m = map(int, input().split())
aa = list(map(int, input().split()))
cc = list(map(int, input().split()))
bb = [None] * (m + 1)

for x in range(m, -1, -1):
    bb[x] = cc[n + x] // aa[n]
    for y in range(n):
        cc[x + y] -= bb[x] * aa[y]
print(*bb)