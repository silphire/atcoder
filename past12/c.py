from collections import defaultdict

pp = [
    list(map(int, input().split()))
    for _ in range(3)
]

d = defaultdict(int)
for i in range(6):
    for j in range(6):
        for k in range(6):
            d[i + j + k + 3] += pp[0][i] * pp[1][j] * pp[2][k]
for i in range(18):
    print(d[i + 1] / 1000000)