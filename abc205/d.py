import bisect

n, q = map(int, input().split())
aa = list(map(int, input().split()))
cc = [0] * n
for i in range(n):
    cc[i] = aa[i] - i - 1
for _ in range(q):
    k = int(input())
    if cc[-1] < k:
        print(aa[-1] + k - cc[-1])
    else:
        p = bisect.bisect_left(cc, k)
        print(aa[p] - 1 - (cc[p] - k))