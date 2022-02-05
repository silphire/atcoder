MOD = 998244353
n = int(input())

r = 1
ans = 0
while n >= r:
    nn = min(r * 10 - 1, n) - r + 1
    ans += (nn + 1) * nn // 2
    ans %= MOD
    r *= 10
print(ans)