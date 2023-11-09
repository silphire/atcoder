x, y = map(int, input().split())

ans = float('inf')
for a in (-1, 1):
    for b in (-1, 1):
        if a * x > b * y:
            continue
        z = 0
        if a == -1:
            z += 1
        z += b * y - a * x
        if b == -1:
            z += 1
        ans = min(ans, z)
print(ans)