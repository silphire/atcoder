import math

n, l, w = map(int, input().split())
aa = list(map(int, input().split())) + [l]

ans = 0
e = 0
for a in aa:
    if e < a:
        ans += (a - e + (w - 1)) // w
    e = a + w
print(ans)