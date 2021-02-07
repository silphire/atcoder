h, w = map(int, input().split())
s = [
    input().rstrip()
    for _ in range(h)
]

ans = 0
for y in range(h - 1):
    for x in range(w - 1):
        n = 0
        if s[y][x] == '#':
            n += 1
        if s[y][x + 1] == '#':
            n += 1
        if s[y + 1][x] == '#':
            n += 1
        if s[y + 1][x + 1] == '#':
            n += 1
        if n == 1 or n == 3:
            ans += 1
print(ans)