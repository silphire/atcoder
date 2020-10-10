h, w = map(int, input().split())
s = [
    input().rstrip()
    for _ in range(h)
]

ans = 0
for y in range(h - 1):
    for x in range(w):
        if s[y][x] == '.' and s[y + 1][x] == '.':
            ans += 1
for y in range(h):
    for x in range(w - 1):
        if s[y][x] == '.' and s[y][x + 1] == '.':
            ans += 1
print(ans)
