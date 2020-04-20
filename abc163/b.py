n, m = map(int, input().split())
aa = list(map(int, input().split()))

s = sum(aa)
if s > n:
    print(-1)
else:
    print(n - s)