import bisect

n, q = map(int, input().split())
rr = list(sorted(map(int, input().split())))
aa = [0] * (n + 1)
for i in range(n):
    aa[i + 1] = aa[i] + rr[i]


for _ in range(q):
    x = int(input())
    if x >= aa[-1]:
        print(n)
    else:
        p = bisect.bisect_left(aa, x)
        if aa[p] != x:
            p -= 1
        print(p)