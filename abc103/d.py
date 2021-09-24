n, m = map(int, input().split())
ab = sorted([
    list(map(int, input().split()))
    for _ in range(m)
], key=lambda x: x[1])
pb = -1
x = 0
for a, b in ab:
    if a >= pb:
        pb = b
        x += 1
print(x)