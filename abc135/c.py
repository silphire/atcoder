n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(n):
    x = min(a[i], b[i])
    ans += x
    a[i] -= x
    b[i] -= x

    ans += min(b[i], a[i + 1])
    a[i + 1] = max(0, a[i + 1] - b[i])
print(ans)
