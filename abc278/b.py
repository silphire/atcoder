h, m = map(int, input().split())

hm = h * 60 + m
while True:
    hh = f'{(hm // 60):02}'
    mm = f'{(hm % 60):02}'
    h2 = int(hh[0] + mm[0])
    m2 = int(hh[1] + mm[1])
    if 0 <= h2 <= 23 and 0 <= m2 < 60:
        print(*[hh, mm])
        break
    hm = (hm + 1) % (24 * 60)