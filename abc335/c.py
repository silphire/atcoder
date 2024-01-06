n, q = map(int, input().split())
d = [(n - i, 0) for i in range(n)]
for _ in range(q):
    op, x = input().split()
    if op == '1':
        if x == 'R':
            d.append((d[-1][0] + 1, d[-1][1]))
        elif x == 'L':
            d.append((d[-1][0] - 1, d[-1][1]))
        elif x == 'U':
            d.append((d[-1][0], d[-1][1] + 1))
        elif x == 'D':
            d.append((d[-1][0], d[-1][1] - 1))
    else:
        p = int(x)
        print(*d[-p])