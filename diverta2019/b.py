r, g, b, n = map(int, input().split())

ans = 0
for x in range(3001):
    if n - r * x < 0:
        break
    for y in range(3001):
        z = n - r * x - g * y
        if z < 0:
            break
        if z % b == 0:
            ans += 1
print(ans)