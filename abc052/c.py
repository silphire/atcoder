from collections import defaultdict

nn = n = int(input())

primes = [x for x in range(1000)]
primes[0] = primes[1] = None
for x in range(2, 1000):
    if primes[x] is None:
        continue
    for y in range(x + x, 1000, x):
        primes[y] = None
primes = list(filter(None, primes))

ctr = defaultdict(int)
for i in range(1, n + 1):
    x = i
    for k in primes:
        while x % k == 0:
            ctr[k] += 1
            x //= k
        if x == 1 or x < k:
            break

ans = 1
for k, v in ctr.items():
    ans *= v + 1
    ans %= 10 ** 9 + 7
print(ans)