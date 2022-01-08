n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]

maxd = 0
for i in range(n):
    for j in range(i + 1, n):
        d = ((xy[i][0] - xy[j][0]) ** 2 + (xy[i][1] - xy[j][1]) ** 2) ** 0.5
        maxd = max(maxd, d)
print(maxd)