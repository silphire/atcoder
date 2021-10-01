n = int(input())
ff = [
    list(map(int, input().split()))
    for _ in range(n)
]
pp = [
    list(map(int, input().split()))
    for _ in range(n)
]

profit = [0] * 10
for j in range(10):
    x = 0
    for i in range(n):
        if ff[i][j] == 1:
            x += 1
    profit[j] = x

ans = float('-inf')
for x in range(1, 1 << 10):
    p = 0
    for j in range(n):
        c = 0
        for i in range(10):
            if x & (1 << i) != 0 and ff[j][i] == 1:
                c += 1
        p += pp[j][c]
    ans = max(ans, p)
print(ans)