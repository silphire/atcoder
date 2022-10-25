a = int(input())
b = int(input())

x = str(a) + str(b // 2)
if b % 2 == 1:
    x += '5'
print(x)