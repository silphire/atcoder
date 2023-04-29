h, w = map(int, input().split())
aa = [
    input()
    for _ in range(h)
]
bb = [
    input()
    for _ in range(h)
]

for sy in range(h):
    for sx in range(w):
        f = True
        for y in range(h):
            for x in range(w):
                if aa[y][x] != bb[(sy + y) % h][(sx + x) % w]:
                    f = False
                    break
            if not f:
                break
        if f:
            print('Yes')
            exit()
print('No')