h, w = map(int, input().split())
r, c = map(int, input().split())

ans = 0
for y in range(1, h + 1):
    for x in range(1, w + 1):
        if abs(c - x) + abs(r - y) == 1:
            ans += 1
print(ans)