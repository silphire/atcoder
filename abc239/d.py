a, b, c, d = map(int, input().split())

primes = [True] * (200 + 1)
primes[0] = primes[1] = False
upper_bound = int(200 ** 0.5) + 1
for i in range(2, upper_bound):
    if not primes[i]:
        continue
    for j in range(2 * i, 200 + 1, i):
        primes[j] = False

for x in range(a, b + 1):
    f = True
    for y in range(c, d + 1):
        if primes[x + y]:
            f = False
            break
    if f:
        print('Takahashi')
        exit()
print('Aoki')