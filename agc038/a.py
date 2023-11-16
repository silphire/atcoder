h, w, a, b = map(int, input().split())

for y in range(h):
    if y < b:
        cl = '0'
        cr = '1'
    else:
        cl = '1'
        cr = '0'
    print((cl * a) + (cr * (w - a)))
