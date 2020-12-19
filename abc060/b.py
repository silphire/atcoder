a, b, c = map(int, input().split())

for n in range(b + 1):
    if n * a % b == c:
        print('YES')
        exit()
print('NO')