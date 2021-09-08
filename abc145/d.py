M = 10 ** 6 + 1
MOD = 10 ** 9 + 7

f = [0] * M
fi = [0] * M
iv = [0] * M

f[0] = f[1] = 1
fi[0] = fi[1] = 1
iv[1] = 1
for i in range(2, M):
    f[i] = f[i - 1] * i % MOD
    iv[i] = MOD - iv[MOD % i] * (MOD // i) % MOD
    fi[i] = fi[i - 1] * iv[i] % MOD

def comb(n, k):
    if n < k or n < 0 or k < 0:
        return 0
    return f[n] * (fi[k] * fi[n - k] % MOD) % MOD

x, y = map(int, input().split())
if (x + y) % 3 == 0:
    a = (x + y) // 3
    b = 2 * a - x
    print(comb(a, b))
else:
    print(0)