n = int(input())
aa = list(map(int, input().split()))

la = [0] * n
la[0] = aa[0]
for i in range(1, n):
    la[i] = max([la[i - 1], aa[i]])
ra = [0] * n
ra[n - 1] = aa[n - 1]
for i in range(n - 1, 0, -1):
    ra[i - 1] = max(ra[i], aa[i - 1])

d = int(input())
for _ in range(d):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    print(max(la[l - 1], ra[r + 1]))