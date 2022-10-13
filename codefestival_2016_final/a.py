h, w = map(int, input().split())
ss = [
    input().rstrip().split()
    for _ in range(h)
]
for y in range(h):
    for x in range(w):
        if ss[y][x] == 'snuke':
            print(chr(ord('A') + x) + str(y + 1))