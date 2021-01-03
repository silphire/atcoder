s, c = map(int, input().split())
x = 0
if c >= s * 2:
    x += s
    c -= s * 2
    s = 0
else:
    x += c // 2
    s -= c // 2
    c = c % 1
x += c // 4
print(x)