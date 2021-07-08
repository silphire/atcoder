n, k = map(int, input().split())
x = 0
x += (k - 1) * (n - k) * 6 
x += (n - 1) * 3
x += 1
print(x / n ** 3)