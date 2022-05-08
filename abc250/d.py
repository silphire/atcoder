def prime_sequence(n: int):
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

pr = prime_sequence(10 ** 6)
npr = len(pr)
n = int(input())

ans = 0
for i in range(npr):
    for j in range(i + 1, npr):
        x = pr[i] * pr[j] ** 3
        if x > n:
            break
        ans += 1
print(ans)