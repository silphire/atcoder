a, m, l, r = map(int, input().split())
l -= a
r -= a
if l % m != 0:
    l += m - l % m
if r % m != 0:
    r -= r % m
print((r - l) // m + 1)