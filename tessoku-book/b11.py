import bisect

n = int(input())
aa = list(sorted(map(int, input().split())))
q = int(input())
for _ in range(q):
    x = int(input())
    print(bisect.bisect_left(aa, x))