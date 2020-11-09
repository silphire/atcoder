x, y = map(int, input().split())
if y == 0:
    print('ERROR')
else:
    z = str(x / y).split('.')
    print(z[0] + "." + (z[1] + '00')[:2])