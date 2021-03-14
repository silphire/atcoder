import math
class Prime(object):
    def __init__(self):
        pass

    def prime_sequence(self, n: int):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        upper_bound = int(n ** 0.5) + 1
        for i in range(2, upper_bound):
            if not primes[i]:
                continue
            for j in range(i * 2, n + 1, i):
                primes[j] = False
        return [i for i in range(2, n + 1) if primes[i]]

n = int(input())
xx = list(map(int, input().split()))
primes = Prime().prime_sequence(50)
ys = []
for i in range(1, 1 << len(primes)):
    y = 1
    for j in range(len(primes)):
        if (i >> j) & 1 == 1:
            y *= primes[j]
    ys.append(y)
ys = sorted(ys)
for y in ys:
    f = True
    for x in xx:
        if math.gcd(x, y) == 1:
            f = False
            break
    if f:
        print(y)
        exit()