n = int(input())
h = list(map(int, input().split()))

ans = 0
x = 0
for i in range(1, n):
    if h[i - 1] >= h[i]:
        x += 1
    else:
        x = 0
    ans = max(ans, x)
print(ans)