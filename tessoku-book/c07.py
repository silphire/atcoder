import bisect

n = int(input())
cc = list(sorted(map(int, input().split())))
for i in range(1, n):
    cc[i] += cc[i - 1]

q = int(input())
for _ in range(q):
    x = int(input())
    p = bisect.bisect_left(cc, x)
    if p < n and cc[p] == x:
        p += 1
    print(p)