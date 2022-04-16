a, b, k = map(int, input().split())
x = 0
while a < b:
    a *= k
    x += 1
print(x)