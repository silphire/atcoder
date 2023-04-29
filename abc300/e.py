from fractions import Fraction

import functools
import sys
sys.setrecursionlimit(10 ** 5)

def modinv(a: int, p: int) -> int:
    """ mod pとした時のaの逆元
    """
    import math
    assert math.gcd(a, p) == 1

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

n = int(input())

@functools.lru_cache(10 ** 6)
def dfs(x):
    global n
    if x == n:
        return Fraction(1, 1)
    elif x > n:
        return Fraction(0, 5)
    else:
        y = Fraction(0, 1)
        for a in range(2, 7):
            y += Fraction(dfs(x * a), 5)
        return y
f = dfs(1)
n = f.numerator
d = f.denominator
MOD = 998244353
ans = n * modinv(d, MOD)
ans %= MOD
print(ans)