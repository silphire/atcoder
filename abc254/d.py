n = int(input())

ans = 0
for i in range(1, n + 1):
    ii = i
    x = 2
    while x * x <= ii:
        while ii % (x * x) == 0:
            ii //= x * x
        x += 1
    x = 1
    while ii * x * x <= n:
        ans += 1
        x += 1
print(ans)