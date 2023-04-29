import bisect
import math

def prime_sequence(n: int):
    """ nまでの素数
    """
    assert n > 0

    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    upper_bound = int(n ** 0.5) + 1
    for i in range(2, upper_bound):
        if not primes[i]:
            continue
        for j in range(2 * i, n + 1, i):
            primes[j] = False
    return [i for i in range(2, n + 1) if primes[i]]

ps = prime_sequence(10 ** 6 + 1)
nps = len(ps)
n = int(input())
ans = 0
for i in range(nps):
    a = ps[i]
    for j in range(i + 1, nps):
        b = ps[j]
        x = a * a * b
        if x > n:
            break
        c = math.floor(math.floor(n / x) ** 0.5)
        k = bisect.bisect_left(ps, c)
        if ps[k] != c:
            k -= 1
        if k - j <= 0:
            break
        ans += k - j
print(ans)
