n, m = map(int, input().split())
rr = [0] * n
bb = [1] * n
rr[0] = 1

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if rr[x] == 1:
        rr[y] = 1
    bb[x] -= 1
    bb[y] += 1
    if bb[x] == 0:
        rr[x] = 0
print(sum(rr))