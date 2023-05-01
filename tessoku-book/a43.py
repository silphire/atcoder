n, l = map(int, input().split())
x = 0
for _ in range(n):
    a, b = input().split()
    a = int(a)
    if b == 'E':
        x = max(x, l - a)
    else:
        x = max(x, a)
print(x)