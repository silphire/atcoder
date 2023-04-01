ss = [
    input()
    for _ in range(8)
]
for y in range(8):
    for x in range(8):
        if ss[y][x] == '*':
            p = chr(ord('a') + x)
            p += str(8 - y)
            print(p)
