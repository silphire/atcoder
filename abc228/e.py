n, k, m = map(int, input().split())
MOD = 998244353
if m % MOD == 0:
    print(0)
else:
    r = pow(k, n, MOD - 1)
    ans = pow(m, r, MOD)
    print(ans)