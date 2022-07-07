M = 998244353

class MOD(object):
    """ mod K 上の演算ライブラリ
    """
    def __init__(self, modulo: int):
        self.modulo = modulo
        self.size = 2
        self.fact = [1, 1]
        self.inv = [0, 1]
        self.finv = [1, 1]

    def comb(self, n: int, k: int) -> int:
        """ nCk (組み合わせ) を求める
        """
        if n < k or n < 0 or k < 0:
            return 0
        if self.size <= n:
            for i in range(self.size, n + 1):
                self.fact.append(self.fact[-1] * i % self.modulo)
                self.inv.append(self.modulo - self.inv[self.modulo % i] * (self.modulo // i) % self.modulo)
                self.finv.append(self.finv[-1] * self.inv[i] % self.modulo)
            self.size = n
        return self.fact[n] * (self.finv[k] * self.finv[n - k] % self.modulo) % self.modulo

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


n, k = map(int, input().split())
aa = list(map(int, input().split()))

if k == 1:
    print(0)
    exit()

mod = MOD(M)
ans = 0
nck = mod.comb(n, k)
for i in range(n - 1):
    x = nck - mod.comb(i + 1, k) - mod.comb(n - i - 1, k)
    x *= (aa[i + 1] - aa[i])
    x %= M
    ans += x
    ans %= M
ans *= MOD.modinv(nck, M)
ans %= M
print(ans)