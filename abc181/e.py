import bisect

n, m = map(int, input().split())
hh = list(sorted(map(int, input().split())))
ww = list(map(int, input().split()))

if n == 1:
    print(min([abs(w - hh[0]) for w in ww]))
    exit()

h1 = [0] * (n // 2)
h2 = [0] * (n // 2)
for i in range(n // 2):
    h1[i] = h1[i - 1] + abs(hh[2 * i] - hh[2 * i + 1])
h2[n // 2 - 1] = abs(hh[n - 1] - hh[n - 2])
for i in range(n // 2 - 2, -1, -1):
    h2[i] = h2[i + 1] + abs(hh[2 * i + 1] - hh[2 * i + 2])
h1 = [0] + h1
h2 = h2 + [0]

ans = float('inf')
for w in ww:
    p = bisect.bisect_left(hh, w)
    if p % 2 == 1:
        ans = min(ans, h1[p // 2] + abs(hh[p - 1] - w) + h2[p // 2])
    else:
        ans = min(ans, h2[p // 2] + abs(hh[p] - w) + h1[p // 2])
print(ans)