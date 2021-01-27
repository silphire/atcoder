n, x = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
if a[0] > x:
    ans += a[0] - x
    a[0] = x
for i in range(1, n):
    d = a[i - 1] + a[i] - x
    if d > 0:
        a[i] -= d
        ans += d
print(ans)