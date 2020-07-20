import itertools

aa = tuple(sorted(map(int, input().split())))
ans = 10 ** 10
for a in itertools.permutations(aa, 3):
    ans = min(ans, abs(a[0] - a[1]) + abs(a[1] - a[2]))
print(ans)
