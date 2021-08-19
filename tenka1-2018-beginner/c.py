n = int(input())
a = sorted([int(input()) for _ in range(n)])

x = a[:n//2]
y = a[(n + 1)//2:]

ans = 0
for i in range(len(x)):
    ans += abs(x[i] - y[i])
for i in range(1, len(y)):
    ans += abs(x[i - 1] - y[i])
if n % 2 == 1:
    ans += max(
        abs(a[n // 2] - x[-1]),
        abs(a[n // 2] - y[0]),
    )
print(ans)