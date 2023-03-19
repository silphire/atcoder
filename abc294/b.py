h, w = map(int, input().split())
aa = [
    list(map(int, input().split()))
    for _ in range(h)
]

ss = ''
for y in range(h):
    for x in range(w):
        if aa[y][x] == 0:
            ss += '.'
        else:
            ss += chr(ord('A') + aa[y][x] - 1)
    ss += "\n"
print(ss)