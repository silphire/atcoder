s = int(input())

p = 10 ** 9
x = (p - s % p) % p
y = (s + x) // p

print(*[0, 0, 10 ** 9, 1, x, y])