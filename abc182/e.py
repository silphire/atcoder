h, w, n, m = map(int, input().split())
mm = [[0] * w for _ in range(h)]
aa = [0] * n
bb = [0] * n
for i in range(n):
    aa[i], bb[i] = map(lambda x: int(x) - 1, input().split())
for i in range(m):
    c, d = map(lambda x: int(x) - 1, input().split())
    mm[c][d] = -1

ans = 0

for i in range(n):
    if mm[aa[i]][bb[i]] == -1:
        continue
    for x in range(bb[i], w):
        b = mm[aa[i]][x]
        if b == -1 or b & 1 == 1:
            break
        if b == 0:
            ans += 1
        mm[aa[i]][x] |= 1
    for x in range(bb[i] - 1, -1, -1):
        b = mm[aa[i]][x]
        if b == -1 or b & 1 == 1:
            break
        if b == 0:
            ans += 1
        mm[aa[i]][x] |= 1

for i in range(n):
    if mm[aa[i]][bb[i]] == -1:
        continue
    for y in range(aa[i], h):
        b = mm[y][bb[i]]
        if b == -1 or b & 2 == 2:
            break
        if b == 0:
            ans += 1
        mm[y][bb[i]] |= 2
    for y in range(aa[i] - 1, -1, -1):
        b = mm[y][bb[i]]
        if b == -1 or b & 2 == 2:
            break
        if b == 0:
            ans += 1
        mm[y][bb[i]] |= 2
print(ans)