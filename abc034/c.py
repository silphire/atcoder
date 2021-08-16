
w, h = map(int, input().split())

n = w + h - 2 + 1
fact = [0] * n
finv = [0] * n
inv = [0] * n

MOD = 10 ** 9 + 7
fact[0] = fact[1] = 1
finv[0] = finv[1] = 1
inv[1] = 1
for x in range(2, n):
    fact[x] = fact[x - 1] * x % MOD
    inv[x] = MOD - inv[MOD % x] * (MOD // x) % MOD
    finv[x] = finv[x - 1] * inv[x] % MOD

x, y = max(w + h - 2, h - 1), min(w + h - 2, h - 1)
ans = fact[x] * (finv[y] * finv[x - y] % MOD) % MOD
print(ans)