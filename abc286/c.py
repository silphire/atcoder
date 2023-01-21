n, a, b = map(int, input().split())
s = input()

ans = float('inf')
for i in range(n):
    x = i * a
    for j in range(n // 2):
        if s[(j + i) % n] != s[(n - 1 - j + i) % n]:
            x += b
    ans = min(ans, x)
print(ans)