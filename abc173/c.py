h, w, k = map(int, input().split())
c = [
    input().rstrip()
    for _ in range(h)
]

ans = 0
for yb in range(2 ** h):
    for xb in range(2 ** w):
        n = 0
        for y in range(h):
            for x in range(w):
                if yb & (1 << y) != 0 and xb & (1 << x) != 0 and c[y][x] == '#':
                    n += 1
        if n == k:
            ans += 1
print(ans)