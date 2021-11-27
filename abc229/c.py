n, w = map(int, input().split())
ab = [None] * n
for i in range(n):
    a, b = map(int, input().split())
    ab[i] = (-a, a, b)
ab.sort()
ans = 0
for x in ab:
    _, a, b = x
    ans += a * min(b, w)
    w = max(0, w - b)
    if w == 0:
        break
print(ans)