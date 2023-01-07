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

primes = prime_sequence(10 ** 7)

t = int(input())
for _ in range(t):
    n = int(input())

    i = 0
    while True:
        x = primes[i]

        y = x * x
        if n % y == 0:
            a = int(y ** 0.5)
            b = n // y
            print(a, b)
            break
        elif n % x == 0:
            b = x
            a = int((n // x) ** 0.5)
            print(a, b)
            break

        i += 1
        if i >= len(primes):
            f = True
            while f:
                x += 1
                f = False
                for p in primes:
                    if x % p == 0:
                        f = True
                        break
            primes.append(x)
