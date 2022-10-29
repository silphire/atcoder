def modinv(a: int, p: int) -> int:
    """ mod pとした時のaの逆元
    """
    b = p
    u = 1
    v = 0
    while b > 0:
        t = a // b

        a -= t * b
        a, b = b, a

        u -= t * v
        u, v = v, u

    u %= p
    if u < 0:
        u += p
    return u

MOD = 998244353
n, m, k = map(int, input().split())

dp = [[0] * (n + 1) for _ in range(k + 1)]
dp[0][0] = 1

for t in range(k):
    dp[t + 1][n] += dp[t][n] * m
    dp[t + 1][n] %= MOD
    for i in range(n):
        if dp[t][i] == 0:
            continue
        for d in range(1, m + 1):
            p = i + d
            if p > n:
                p = n - (p - n)
            dp[t + 1][p] += dp[t][i]
            dp[t + 1][p] %= MOD
ans = dp[k][n] * modinv(sum(dp[k]) % MOD, MOD)

ans %= MOD
print(ans)