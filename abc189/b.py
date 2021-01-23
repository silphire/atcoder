n, x = map(int, input().split())
a = 0
x *= 100
for i in range(n):
    v, p = map(int, input().split())
    a += v * p
    if a > x:
        print(i + 1)
        exit()
print(-1)