n, s, t = map(int, input().split())
w = int(input())
ans = int(s <= w <= t)
for i in range(2, n + 1):
    a = int(input())
    w += a
    if s <= w <= t:
        ans += 1
print(ans)