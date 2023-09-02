n, m, p = map(int, input().split())
x = 0
d = m
while d <= n:
    x += 1
    d += p
print(x)