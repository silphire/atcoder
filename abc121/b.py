n, m, c = map(int, input().split())
b = tuple(map(int, input().split()))
ans = 0
for i in range(n):
    a = tuple(map(int, input().split()))
    x = 0
    for j in range(m):
        x += a[j] * b[j]
    if x + c > 0:
        ans += 1
print(ans)