n = int(input())
f = [[0] * 101 for _ in range(101)]
ans = 0
for _ in range(n):
    a, b, c, d = map(int, input().split())
    for x in range(a, b):
        for y in range(c, d):
            if f[y][x] == 0:
                ans += 1
            f[y][x] += 1
print(ans)