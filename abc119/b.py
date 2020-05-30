C = 380000.0

ans = 0.0
n = int(input())
for i in range(n):
    x, u = input().split()
    if u == 'JPY':
        ans += int(x)
    else:
        ans += float(x) * C
print(ans)
