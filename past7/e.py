n = int(input())

for k in range(30):
    x = 1
    for i in range(30):
        x *= 3
        if i == k:
            x += 1
    if n == x:
        print(k + 1)
        exit()
print(-1)