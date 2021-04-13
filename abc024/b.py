n, t = map(int, input().split())
a = [int(input()) for _ in range(n)]
ans = 0
for i in range(1, n):
    ans += min(t, a[i] - a[i - 1])
print(ans + t)