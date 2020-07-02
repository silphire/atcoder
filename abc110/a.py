import itertools

aa = tuple(map(int, input().split()))
ma = 0
for a in itertools.permutations(aa, 3):
    ma = max(ma, a[0] * 10 + a[1] + a[2])
print(ma)
