a, b, c = map(int, input().split())

if c % 2 == 1:
    if a < b:
        print('<')
    elif a > b:
        print('>')
    else:
        print('=')
else:
    a = a * a
    b = b * b
    if a < b:
        print('<')
    elif a > b:
        print('>')
    else:
        print('=')
