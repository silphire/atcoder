from decimal import Decimal, ROUND_HALF_UP

dir = (
    ('N', 0, 1125),
    ('NNE', 1125, 3375),
    ('NE', 3375, 5625),
    ('ENE', 5625, 7875), 
    ('E', 7875, 10125),
    ('ESE', 10125, 12375),
    ('SE', 12375, 14625),
    ('SSE', 14625, 16875),
    ('S', 16875, 19125),
    ('SSW', 19125, 21375),
    ('SW', 21375, 23625),
    ('WSW', 23625, 25875),
    ('W', 25875,  28125),
    ('WNW', 28125, 30375),
    ('NW', 30375, 32625),
    ('NNW', 32625, 34875),
    ('N', 34875, 36000),
)

wp = (
    (0, 2),
    (3, 15),
    (16, 33),
    (34, 54),
    (55, 79),
    (80, 107),
    (108, 138),
    (139, 171),
    (172, 207),
    (208, 244),
    (245, 284),
    (285, 326),
)

deg, dis = map(int, input().split())
deg *= 10
dis = (Decimal(dis) / 6).quantize(Decimal(0), rounding=ROUND_HALF_UP)

d = ''
for dd in dir:
    if dd[1] <= deg < dd[2]:
        d = dd[0]
        break

w = 0
for ww in wp:
    if ww[0] <= dis <= ww[1]:
        break
    w += 1

if w == 0:
    print('C 0')
else:
    print(f'{d} {w}')