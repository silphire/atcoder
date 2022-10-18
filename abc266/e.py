n = int(input())

f = [0] * (n + 1)
f[1] = 21 / 6
for x in range(2, n + 1):
    f[x] = 0
    for y in range(1, 7):
        f[x] += max(y, f[x - 1])
    f[x] /= 6
print(f[n])