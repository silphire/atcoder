n = int(input())
ans = float('inf')
for i in range(n):
    a, p, x = map(int, input().split())
    if a < x:
        ans = min(ans, p)

if ans > 10 ** 9:
    print(-1)
else:
    print(ans)