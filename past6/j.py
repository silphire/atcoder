n, c = map(int, input().split())
x = [0] * n
y = [0] * n
for i in range(n):
    x[i], y[i] = map(int, input().split())

l = -1e6
r = 1e6
mincost = float('inf')
while r - l > 1e-12:
    m = (l + r) / 2
    cl = 0
    cr = 0
    for i in range(n):
        cl += (l - x[i]) ** 2 + (c - y[i]) ** 2
        cr += (r - x[i]) ** 2 + (c - y[i]) ** 2
    if cl < cr:
        r = m
    else:
        l = m
print(cl)
