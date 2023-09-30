import bisect

n, m = map(int, input().split())
aa = list(map(int, input().split()))

for i in range(1, n + 1):
    p = bisect.bisect_left(aa, i)
    print(aa[p] - i)