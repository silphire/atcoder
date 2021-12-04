n, d = map(int, input().split())
sect = sorted([
    tuple(map(int, input().split()))
    for _ in range(n)
], key=lambda x: x[1])

ans = 0
prev = float('-inf')
for l, r in sect:
    if prev + d - 1 < l:
        ans += 1
        prev = r
print(ans)