n = int(input())

r = 1
f = [True] * (2 * n + 2)
while r <= 2 * n + 1:
    while not f[r]:
        r += 1
    print(r, flush=True)
    f[r] = False
    r += 1

    x = int(input())
    f[x] = False
    if x == 0:
        break