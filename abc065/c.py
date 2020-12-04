M = 10 ** 9 + 7
n, m = map(int, input().split())
d = abs(n - m)
if d > 1:
    print(0)
    exit()
x = 1
for a in range(2, n + 1):
    x *= a
    x %= M
y = 1
for a in range(2, m + 1):
    y *= a
    y %= M
print(x * y * (2 - d) % M)