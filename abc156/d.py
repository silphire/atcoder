import math

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

M = 10 ** 9 + 7
n, a, b = map(int, input().split())

def comb(x):
    global n, a, b
    r = 1
    for i in range(x):
        r *= n - i
        r %= M
    for i in range(x):
        r *= modinv(i + 1, M)
        r %= M
    return r


ans = pow(2, n, M) - 1
ans -= comb(a)
while ans < 0:
    ans += M
ans -= comb(b)
while ans < 0:
    ans += M
print(ans)