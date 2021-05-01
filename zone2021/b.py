n, x2, y2 = map(int, input().split())
ans = 0
for i in range(n):
    x1, y1 = map(int, input().split())
    if x1 > x2:
        continue
    if x1 == x2:
        b = y2
    else:
        a = (y2 - y1) / (x2 - x1)
        b = (x1 * y2 - x2 * y1) / (x1 - x2)
    ans = max(ans, b)
print(ans)