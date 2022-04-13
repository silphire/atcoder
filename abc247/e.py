n, x, y = map(int, input().split())
aa = list(map(int, input().split()))

px = -1
py = -1
inv = -1
ans = 0

for i, a in enumerate(aa):
    if a == x:
        px = i
    if a == y:
        py = i
    if a < y or x < a:
        inv = i
    ans += max(0, min(px, py) - inv)
print(ans)