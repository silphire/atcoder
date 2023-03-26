import bisect

n, x = map(int, input().split())
aa = list(map(int, input().split()))

print(bisect.bisect_left(aa, x) + 1)