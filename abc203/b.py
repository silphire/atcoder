n, k = map(int, input().split())
ans = 0
for x in range(1, n + 1):
    for y in range(1, k + 1):
        ans += x * 100 + y
print(ans)
