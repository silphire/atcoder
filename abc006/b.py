n = int(input())
f = [0] * (max(3, n) + 1)
f[3] = 1
for i in range(4, n + 1):
    f[i] = f[i - 1] + f[i - 2] + f[i - 3]
    f[i] %= 10007
print(f[n])