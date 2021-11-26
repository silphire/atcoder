n, d = map(int, input().split())
MOD = 998244353
N = 10 ** 6

p2 = [0] * (2 * N + 1)
p2[0] = 1
for i in range(1, 2 * N + 1):
    p2[i] = p2[i - 1] * 2
    p2[i] %= MOD

ans = 0
for i in range(n):
    if i + d <= n - 1:
        f1 = p2[d + 1]
    else:
        f1 = 0
    if d == 1 or 2 * (n - 1 - i) < d:
        f2 = 0
    elif i + d <= n - 1:
        f2 = p2[d - 1] * (d - 1)
    else:
        f2 = p2[d - 1] * (2 * n - 2 * i - d - 1)
    ans += p2[i] * (f1 + f2)
    ans %= MOD
print(ans)
