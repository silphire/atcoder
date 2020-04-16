a, b = map(int, input().split())
n = 0
m = 1
while m < b:
    n += 1
    m += a - 1
if n > 0:
    m += 1

print(n)
