n = list(map(int, list(input().rstrip())))

ans = sum(n)
for i in range(len(n)):
    x = 0
    for j in range(len(n)):
        if j < i:
            x += n[j]
        elif j == i:
            x += n[j] - 1
        else:
            x += 9
    ans = max(ans, x)
print(ans)