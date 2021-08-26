n, c = map(int, input().split())
N = 10 ** 5 + 1
x = [[0] * N for _ in range(30)]
for i in range(n):
    s, t, c = map(int, input().split())
    s -= 1
    c -= 1
    x[c][s] += 1
    x[c][t] -= 1
for j in range(30):
    for i in range(1, N):
        x[j][i] += x[j][i - 1]
for j in range(30):
    for i in range(N):
        if x[j][i] > 0:
            x[j][i] = 1
ans = 0
for i in range(N):
    a = 0
    for j in range(30):
        a += x[j][i]
    ans = max(ans, a)
print(ans)