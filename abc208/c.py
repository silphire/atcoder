n, k = map(int, input().split())
aa = list(map(int, input().split()))

ans = k // n
k %= n

m = sorted(aa)[k]
for a in aa:
    r = int(a < m)
    print(ans + r)