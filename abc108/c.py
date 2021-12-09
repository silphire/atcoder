n, k = map(int, input().split())

ans = 0

m = 0
for x in range(1, n + 1):
    if x % k == 0:
        m += 1
ans += m ** 3

if k % 2 == 0:
    m = 0
    for x in range(1, n + 1):
        if x % k == k // 2:
            m += 1
    ans += m ** 3

print(ans)