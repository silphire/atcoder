t, n = map(int, input().split())
pp = [
    list(map(int, input().split()))
    for _ in range(t)
]

cc = [0] * n
for i in range(t):
    for j in range(n):
        cc[j] = max(cc[j], pp[i][j])
    print(sum(cc))