n = int(input())
p = 1
for i in range(1, n + 1):
    p *= i
    p %= 10 ** 9 + 7
print(p)