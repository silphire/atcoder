n, k = map(int, input().split())

ans = 0.0
for x in range(1, n + 1):
    y = x
    m = 0
    while y <= k - 1:
        m += 1
        y *= 2
    ans += 1 / (2 ** m)
print(ans / n)