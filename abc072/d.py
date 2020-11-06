n = int(input())
pp = list(map(int, input().split()))

ans = 0
for i in range(n):
    if i + 1 == pp[i]:
        ans += 1
        if i < n - 1:
            pp[i], pp[i + 1] = pp[i + 1], pp[i]
print(ans)
