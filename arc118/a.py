t, n = map(int, input().split())
x = n * 100
y = (x + t - 1) // t
print(y + (t * y // 100) - 1)