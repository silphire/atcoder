n, m = map(int, input().split())
a = [0] * n
b = [0] * m
for i in range(n):
    a[i] = input().rstrip()
for i in range(m):
    b[i] = input().rstrip()

if n < m:
    print('No')
    exit()

for y in range(n - m + 1):
    for x in range(n - m + 1):
        f = False
        for j in range(m):
            for i in range(m):
                if a[y + j][x + i] != b[j][i]:
                    f = True
                    break
            if f:
                break
        if not f:
            print('Yes')
            exit()
print('No')