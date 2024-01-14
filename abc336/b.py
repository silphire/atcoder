n = int(input())
x = 0
while n > 0 and n & 1 == 0:
    x += 1
    n >>= 1
print(x)
