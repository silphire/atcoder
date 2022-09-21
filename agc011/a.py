n, c, k = map(int, input().split())
tt = sorted([int(input()) for _ in range(n)], reverse=True)
ans = 0
np = 0
x = None
for t in tt:
    if x is None or t + k < x or np == c:
        ans += 1
        x = t
        np = 0
    np += 1
print(ans)