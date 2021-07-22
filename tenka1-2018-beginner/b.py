a, b, k = map(int, input().split())
for i in range(k):
    if i & 1 == 0:
        if a & 1 == 1:
            a -= 1
        b += a // 2
        a //= 2
    else:
        if b & 1 == 1:
            b -= 1
        a += b // 2
        b //= 2
print(f'{a} {b}')