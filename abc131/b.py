n, l = map(int, input().split())

# L ~ L + N - 1

y = 1000000000000
xx = None
for x in range(l, l + n):
    if y > abs(x):
        y = abs(x)
        xx = x

ans = 0
for x in range(l, l + n):
    if x == xx:
        continue
    ans += x
print(ans)