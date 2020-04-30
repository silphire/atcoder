def dist(x, y):
    d = 0.0
    for i in range(len(x)):
        d += (x[i] - y[i]) ** 2
    return d ** 0.5

n, d = map(int, input().split())
x = []
for i in range(n):
    x.append(tuple(map(int, input().split())))

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        d = dist(x[i], x[j])
        if abs(d - int(d)) < 1e-6:
            ans += 1
print(ans)
