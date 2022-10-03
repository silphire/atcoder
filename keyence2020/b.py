n = int(input())
ds = [
    list(map(int, input().split()))
    for _ in range(n)
]

ds = sorted([
    (x, x + l, l)
    for x, l in ds
], key=lambda a: (a[1], a[2]))

px = float('-inf')
ans = 0
for x, y, l in ds:
    if px <= x - l:
        px = y
        ans += 1
print(ans)