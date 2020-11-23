a, b, c = map(int, input().split())

INF = 10000

dp = [[[INF] * 101 for _ in range(101)] for _ in range(101)]
for i in range(100):
    for j in range(100):
        dp[100][i][j] = 0
        dp[i][100][j] = 0
        dp[i][j][100] = 0

def f(x, y, z):
    if dp[x][y][z] != INF:
        return dp[x][y][z]
    a = 0.0
    d = 1.0 / (x + y + z)
    a += x * d * (f(x + 1, y, z) + 1)
    a += y * d * (f(x, y + 1, z) + 1)
    a += z * d * (f(x, y, z + 1) + 1)
    dp[x][y][z] = a
    return a

print(f(a, b, c))
