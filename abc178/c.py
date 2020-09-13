M = 10 ** 9 + 7
n = int(input())

if n <= 1:
    print(0)
    exit()

nones = 8
zero = 1
nine = 1
other = 0
for x in range(1, n):
    other = other * 10 + zero + nine
    zero = zero * 9 + nones
    nine = nine * 9 + nones
    nones *= 8

    other %= M
    zero %= M
    nine %= M
    nones %= M

print(other)