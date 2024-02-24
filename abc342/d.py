from collections import Counter
from collections import defaultdict
import math

def prime_factorize(n: int):
    """ nを素因数分解する
    """
    spf = [1] * (n + 1)
    spf[0] = 0
    for i in range(2, n + 1):
        if spf[i] != 1:
            continue
        for j in range(i, n + 1, i):
            spf[j] = i

    f = defaultdict(int)
    while n > 1:
        s = spf[n]
        f[s] += 1
        n //= s
    return f

def prime_sequence(n: int) -> list[int]:
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


primes = prime_sequence(200000)
tb = [defaultdict(bool) for _ in range(200001)]
for p in primes:
    x = p
    f = True
    while x <= 200000:
        y = x
        while y <= 200000:
            tb[y][p] = f
            y += x
        x *= p
        f = not f
tb = [frozenset([a for a, f in tb[x].items() if f]) for x in range(200001)]

n = int(input())
aa = list(map(int, input().split()))
bb = []
z = 0

for a in aa:
    if a == 0:
        z += 1
    else:
        bb.append(frozenset(tb[a]))

ans = 0
for b in range(z):
    ans += n - b - 1

ctr = Counter(bb)
for x, num in ctr.items():
    ans += math.comb(num, 2)
print(ans)