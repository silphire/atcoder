n = int(input())
ans = 0
for a in range(1, n + 1):
    for b in range(a, n + 1):
        if a * b < n:
            if a == b:
                ans += 1
            else:
                ans += 2
        else:
            break
print(ans)
