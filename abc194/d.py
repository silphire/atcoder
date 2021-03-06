n = int(input())

ans = 0
for x in range(1, n + 1):
    ans += 1 / x
print(ans * n - 1)