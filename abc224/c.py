n = int(input())
r = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            a = (r[i][0] - r[k][0]) * (r[j][1] - r[k][1]) - (r[j][0] - r[k][0]) * (r[i][1] - r[k][1])
            a = abs(a) / 2
            if a > 0:
                ans += 1
print(ans)