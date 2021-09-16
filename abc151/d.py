h, w = map(int, input().split())
ans = 0
s = []
a = []
q = []
for i in range(h):
    s.append(input())


for yy in range(h):
    for xx in range(w):
        a = []
        for i in range(h):
            a.append([0] * w)

        d = 1
        q = [(xx, yy)]
        while True:
            nq = []
            while len(q) > 0:
                p = q.pop()
                x, y = p
                if x < 0 or x >= w or y < 0 or y >= h:
                    continue
                if s[y][x] == '#':
                    continue
                if a[y][x] > 0:
                    continue
                a[y][x] = d
                nq.append((x - 1, y))
                nq.append((x + 1, y))
                nq.append((x, y - 1))
                nq.append((x, y + 1))
            if len(nq) == 0:
                break
            q = nq
            d += 1

        b = []
        for i in range(h):
            b.extend(a[i])
        b = sorted(b, reverse=True)
        ans = max(ans, b[0])
print(ans - 1)
