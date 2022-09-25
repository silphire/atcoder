h, w = map(int, input().split())
ss = [
    list(map(int, input().split()))
    for _ in range(h)
]

n = int(input())
for i in range(n):
    r, c = map(int, input().split())
    r -= 1
    c -= 1

    ss[r][c] = 0
    for a in range(r, 0, -1):
        ss[a][c] = ss[a - 1][c]
    ss[0][c] = 0

for s in ss:
    print(*s)