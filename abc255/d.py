import bisect

n, q = map(int, input().split())
aa = list(sorted(map(int, input().split())))
ac = [0] * (n + 1)
for i in range(n):
    ac[i + 1] = ac[i] + aa[i]
xx = [int(input()) for _ in range(q)]
for x in xx:
    p = bisect.bisect_right(aa, x)
    ans = x * p - ac[p] + (ac[-1] - ac[p] - x * (n - p))
    print(ans)