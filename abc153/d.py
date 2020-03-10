h = int(input())

n = 0
while h >= 1:
    n += 1
    h /= 2
print((1 << n) - 1)
