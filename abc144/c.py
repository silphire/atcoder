n = int(input())

ans = n + 1
for x in range(1, int(n ** 0.5) + 2):
    if n % x != 0:
        continue
    y = n // x
    ans = min(ans, x + y - 2)
print(ans)