n = int(input())
ans = 0
x = [0] * n
y = [0] * n
for i in range(n):
    x[i], y[i] = map(int, input().split())

for i in range(n):
    for j in range(i + 1, n):
        if abs(y[j] - y[i]) / abs(x[j] - x[i]) <= 1:
            ans += 1
print(ans)