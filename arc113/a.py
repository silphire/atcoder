k = int(input())
ans = 0
for a in range(1, k + 1):
    for b in range(1, k + 1):
        x = a * b
        if x > k:
            break
        ans += k // x
print(ans)