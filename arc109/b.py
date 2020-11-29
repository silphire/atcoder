n = int(input())

x1 = 1
x2 = n + 1
while x2 - x1 > 1:
    x = (x1 + x2) // 2
    if x * (x + 1) // 2 <= n + 1:
        x1 = x
    else:
        x2 = x
print(n - x1 + 1)