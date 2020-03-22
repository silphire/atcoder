n, m = map(int, input().split())

x = 0
for i in range(n + m):
    for j in range(n + m):
        if i == j:
            continue
        x1 = i < n
        x2 = j < n
        if (x1 and x2) or (not x1 and not x2):
            x += 1
print(x // 2)
