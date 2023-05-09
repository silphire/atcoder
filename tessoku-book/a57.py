n, q = map(int, input().split())
aa = list(map(lambda x: int(x) - 1, input().split()))
for _ in range(q):
    x, y = map(int, input().split())
    x -= 1

    d = 1
    z = aa[x]
    while z != x:
        d += 1
        z = aa[z]

    y %= d
    while y > 0:
        x = aa[x]
        y -= 1
    print(x + 1)