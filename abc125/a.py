a, b, t = map(int, input().split())

tt = 0
x = 0
while True:
    tt += a
    if tt > t + 0.5:
        break
    x += b
print(x)