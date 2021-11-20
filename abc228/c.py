import bisect

n, k = map(int, input().split())
pp = [
    sum(map(int, input().split()))
    for _ in range(n)
]

sp = sorted(pp)
for i in range(n):
    x = bisect.bisect_right(sp, pp[i] + 300)
    if n - x + 1 <= k:
        print('Yes')
    else:
        print('No')