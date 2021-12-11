import bisect
n, q = map(int, input().split())
aa = list(sorted(map(int, input().split())))
xx = [int(input()) for _ in range(q)]
for x in xx:
    p = bisect.bisect_left(aa, x)
    print(n - p)
