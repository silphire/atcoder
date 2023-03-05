n, q = map(int, input().split())
m = [0] * (n + 1)
for _ in range(q):
    e, x = map(int, input().split())
    if e == 1:
        m[x] += 1
    elif e == 2:
        m[x] += 2
    else:
        if m[x] >= 2:
            print('Yes')
        else:
            print('No')