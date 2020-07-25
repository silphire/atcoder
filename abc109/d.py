h, w = map(int, input().split())
aa = [
    list(map(int, input().split()))
    for _ in range(h)
]

ans = []
for y in range(h):
    for x in range(w - 1):
        if aa[y][x] & 1 == 1:
            ans.append((y, x, y, x + 1))
            aa[y][x] -= 1
            aa[y][x + 1] += 1
for y in range(h - 1):
    if aa[y][w - 1] & 1 == 1:
        ans.append((y, w - 1, y + 1, w - 1))
        aa[y][w - 1] -= 1
        aa[y + 1][w - 1] += 1

print(len(ans))
for a in ans:
    print(' '.join(map(lambda x: str(x + 1), a)))