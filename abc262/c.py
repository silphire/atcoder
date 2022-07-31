n = int(input())
aa = list(map(int, input().split()))

x = 0
y = 0
for i in range(n):
    if aa[i] == i + 1:
        x += 1
    elif aa[aa[i] - 1] == i + 1:
        y += 1
ans = x * (x - 1) // 2 + y // 2
print(ans)
