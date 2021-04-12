n, a, b = map(int, input().split())
x = 0
for i in range(n):
    s, d = input().rstrip().split()
    d = int(d)
    if s == 'East':
        s = -1
    else:
        s = 1
    if d < a:
        x = x + a * s
    elif d > b:
        x = x + b * s
    else:
        x = x + d * s
if x < 0:
    y = "East "
elif x > 0:
    y = "West "
else:
    y = ""
print(f'{y}{abs(x)}')