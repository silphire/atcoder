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

for x in prime_sequence(int(input())):
    print(x)