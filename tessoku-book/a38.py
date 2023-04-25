d, n = map(int, input().split())
ans = [24] * d
for _ in range(n):
    l, r, h = map(int, input().split())
    l -= 1
    r -= 1
    for x in range(l, r + 1):
        ans[x] = min(ans[x], h)
print(sum(ans))