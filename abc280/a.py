h, w = map(int, input().split())
s = [
    input()
    for _ in range(h)
]
a = 0
for y in range(h):
    for x in range(w):
        if s[y][x] == '#':
            a += 1
print(a)