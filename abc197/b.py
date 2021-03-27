h, w, x, y = map(int, input().split())
s = [
    input().rstrip()
    for _ in range(h)
]
x -= 1
y -= 1
x, y = y, x

ans = 1

xx = x - 1
while xx >= 0 and s[y][xx] == '.':
    ans += 1
    xx -= 1
xx = x + 1
while xx < w and s[y][xx] == '.':
    ans += 1
    xx += 1
yy = y - 1
while yy >= 0 and s[yy][x] == '.':
    ans += 1
    yy -= 1
yy = y + 1
while yy < h and s[yy][x] == '.':
    ans += 1
    yy += 1
print(ans)