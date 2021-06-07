n, m = map(int, input().split())

# b + 2c = m - 2n
k = m - 2 * n
for b in range(n + 1):
    if (m - 2 * n - b) % 2 == 1:
        continue
    c = (m - 2 * n - b) // 2
    if c < 0:
        continue
    a = n - b - c
    if a >= 0:
        print(f'{a} {b} {c}')
        exit()
print('-1 -1 -1')