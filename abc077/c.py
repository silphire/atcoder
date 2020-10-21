import bisect

n = int(input())
aa = list(sorted(map(int, input().split())))
bb = list(sorted(map(int, input().split())))
cc = list(sorted(map(int, input().split())))

bm = [0] * n
for ib in range(n):
    c = bisect.bisect_left(cc, bb[ib] + 1)
    if c == n:
        continue
    bm[ib] = n - c
for i in range(n - 2, -1, -1):
    bm[i] += bm[i + 1]

am = [0] * n
for ia in range(n):
    b = bisect.bisect_left(bb, aa[ia] + 1)
    if b == n:
        continue
    am[ia] = bm[b]

print(sum(am))
