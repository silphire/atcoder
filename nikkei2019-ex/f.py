p = int(input())

# f(x) = f(x/2) + 1
# f(x) = f(3x + 1) + 1

# f(1000) = 1789997546303
x = 1789997546303
y = 1000
while y > p:
    if x % 2 == 0:
        x //= 2
    else:
        x = 3 * x + 1
    y -= 1
print(x)
