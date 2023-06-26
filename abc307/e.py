MOD = 998244353
n, m = map(int, input().split())
ans = m - 1
if n % 2 == 1:
    ans *= -1
ans += pow(m - 1, n, MOD)
ans %= MOD
print(ans)
