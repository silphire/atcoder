n, a, b = map(int, input().split())
xx = list(map(int, input().split()))

ans = 0
for i in range(n - 1):
    d = xx[i + 1] - xx[i]
    if d * a > b:
        ans += b
    else:
        ans += (d * a)
print(ans)