from collections import Counter
from fractions import Fraction

k = int(input())
s = input().rstrip()
t = input().rstrip()

s = Counter(map(int, list(s)[:4]))
t = Counter(map(int, list(t)[:4]))
remain = {i: k - s[i] - t[i] for i in range(1, 10)}
nr = sum(remain.values())

ss = sum([i * (10 ** s[i]) for i in range(1, 10)])
tt = sum([i * (10 ** t[i]) for i in range(1, 10)])

ans = Fraction(0, 1)
for x in range(1, 10):
    for y in range(1, 10):
        if x == y:
            if remain[x] < 2:
                continue
        else:
            if remain[x] < 1 or remain[y] < 1:
                continue

        ns = ss - x * 10 ** s[x] + x * 10 ** (s[x] + 1)
        nt = tt - y * 10 ** t[y] + y * 10 ** (t[y] + 1)
        if ns > nt:
            if x == y:
                ans += Fraction(remain[x], nr) * Fraction(remain[x] - 1, nr - 1)
            else:
                ans += Fraction(remain[x], nr) * Fraction(remain[y], nr - 1)

print(float(ans))