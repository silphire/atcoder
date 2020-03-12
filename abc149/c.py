import math

x = int(input())

primes = []

if x == 2:
    print(2)
    exit(0)

for n in range(3, 10000000000, 2):
    f = True
    mp = math.ceil(math.sqrt(n))
    for p in primes:
        if p > mp:
            break
        if n % p == 0:
            f = False
            break
    if f:
        primes.append(n)
        if n >= x:
            print(n)
            exit(0)
