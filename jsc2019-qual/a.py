m, d = map(int, input().split())
x = 0
for mm in range(1, m + 1):
    for dd in range(20, d + 1):
        d1 = dd % 10
        d10 = dd // 10
        if d1 >= 2 and d10 >= 2 and d1 * d10 == mm:
            x += 1
print(x)