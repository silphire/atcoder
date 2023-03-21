n, k = map(int, input().split())
ans = 0
for x in range(1, n + 1):
    for y in range(1, n + 1):
        if k - x - y > n:
            continue
        if x + y >= k:
            break
        ans += 1
print(ans)