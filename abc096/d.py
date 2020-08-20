import itertools

n = int(input())
primes = [x for x in range(3, 55556, 2)]

for i in range(3, 237, 2):
    for j, p in enumerate(primes):
        if p <= i:
            continue
        if p % i == 0:
            primes[j] = 0
primes = [2] + [p for p in primes if p > 0]
aa = [p for p in primes if p <= 55555 and p % 5 == 1]
print(' '.join(map(str, aa[:n])))
