n, q = map(int, input().split())
s = input().rstrip()
h = 0
for _ in range(q):
    c, x = map(int, input().split())
    if c == 1:
        h -= x
        while h < 0:
            h += n
    else:
        print(s[(h + x - 1) % n])