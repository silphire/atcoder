h, w = map(int, input().split())
c = [
    list(map(int, input().split()))
    for _ in range(10)
]
a = [
    list(map(int, input().split()))
    for _ in range(h)
]

for k in range(10):
    for i in range(10):
        for j in range(10):
            c[i][j] = min(c[i][j], c[i][k] + c[k][j])

ans = 0
for y in range(h):
    for x in range(w):
        if a[y][x] == -1:
            continue
        d = a[y][x]
        ans += c[d][1]
print(ans)