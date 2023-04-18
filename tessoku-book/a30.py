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
        m = self.modulo
        if self.size <= n:
            for i in range(self.size, n + 1):
                self.fact.append(self.fact[-1] * i % m)
                self.inv.append(m - self.inv[m % i] * (self.modulo // i) % m)
                self.finv.append(self.finv[-1] * self.inv[i] % m)
            self.size = n
        return self.fact[n] * (self.finv[k] * self.finv[n - k] % m) % m

print(MOD(1000000007).comb(*map(int, input().split())))