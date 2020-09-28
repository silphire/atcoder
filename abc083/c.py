x, y = map(int, input().split())
n = 0
while x <= y:
    x += x
    n += 1
print(n)