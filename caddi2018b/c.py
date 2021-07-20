from collections import defaultdict

n, p = map(int, input().split())

pp = p
d = defaultdict(int)
for x in range(2, int(p ** 0.5) + 1):
    while pp % x == 0:
        d[x] += 1
        pp //= x
if pp > 1:
    d[pp] += 1

ans = 1
for k, v in d.items():
    ans *= k ** (v // n)
print(ans)