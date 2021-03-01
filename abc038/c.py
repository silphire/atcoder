n = int(input())
a = list(map(int, input().split()))

ans = 0
p = 0
for i in range(1, n):
    if a[i - 1] >= a[i]:
        x = i - p
        ans += (x + 1) * x // 2
        p = i

x = n - p
ans += (x + 1) * x // 2
print(ans)