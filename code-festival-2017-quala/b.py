n, m, k = map(int, input().split())

for j in range(m):
    for i in range(n):
        x = i * m + j * n - 2 * i * j
        if x == k:
            print('Yes')
            exit()
print('No')