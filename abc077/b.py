n = int(input())
x = 1
y = 1
while y <= n:
    x += 1
    y = x * x
x -= 1
print(x * x)