a, b, c, d, e, f, x = map(int, input().split())

dt = a * b * (x // (a + c))
rt = x % (a + c)
dt += min(rt, a) * b

da = d * e * (x // (d + f))
ra = x % (d + f)
da += min(ra, d) * e

if da < dt:
    print('Takahashi')
elif da > dt:
    print('Aoki')
else:
    print('Draw')