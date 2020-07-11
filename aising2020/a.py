l, r, d = map(int, input().split())
ans = 0
for x in range(l, r + 1):
    if x % d == 0:
        ans += 1
print(ans)
