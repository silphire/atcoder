N = 1501
n = int(input())
field = [[0] * N for _ in range(N)]
ans = 0
for _ in range(n):
    a, b, c, d = map(int, input().split())
    field[b][a] += 1
    field[b][c] -= 1
    field[d][a] -= 1
    field[d][c] += 1
for y in range(N):
    for x in range(N):
        if x == 0:
            continue
        field[y][x] += field[y][x - 1]
    if y == 0:
        continue
    for x in range(N):
        field[y][x] += field[y - 1][x]
ans = 0
for y in range(N):
    for x in range(N):
        if field[y][x] > 0:
            ans += 1
print(ans)