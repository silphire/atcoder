n, m, d = map(int, input().split())
if d == 0:
    ans = 1 / n
else:
    ans = 2 * (n - d) / n / n
ans *= m - 1
print(ans)