n = int(input())
aa = [
    list(map(int, list(input().rstrip())))
    for _ in range(n)
]

ans = 0
for y in range(n):
    for x in range(n):
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                d = 0
                for i in range(n):
                    px = x + i * dx
                    while px < 0:
                        px += n
                    px %= n

                    py = y + i * dy
                    while py < 0:
                        py += n
                    py %= n
                    d = d * 10 + aa[py][px]
                ans = max(ans, d)
print(ans)