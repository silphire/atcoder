r, c = map(int, input().split())
s = [
    'ooooooooooooooo',
    'o.............o',
    'o.ooooooooooo.o',
    'o.o.........o.o',
    'o.o.ooooooo.o.o',
    'o.o.o.....o.o.o',
    'o.o.o.ooo.o.o.o',
    'o.o.o.o.o.o.o.o',
    'o.o.o.ooo.o.o.o',
    'o.o.o.....o.o.o',
    'o.o.ooooooo.o.o',
    'o.o.........o.o',
    'o.ooooooooooo.o',
    'o.............o',
    'ooooooooooooooo',
]
r -= 1
c -= 1
if s[r][c] == 'o':
    print('black')
else:
    print('white')