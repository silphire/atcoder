a, b, c, d = map(int, input().split())
x = a / b
y = c / d
if x < y:
    print('<')
elif x > y:
    print('>')
else:
    print('=')