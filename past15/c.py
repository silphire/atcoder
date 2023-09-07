import math
x, y, r, n = map(int, input().split())
ss = ''
for i in range(-n, n + 1):
    if ss:
        ss += "\n"
    s = ''
    for j in range(-n, n + 1):
        if math.dist((x, y), (i, j)) <= r:
            s += '# '
        else:
            s += '. '
    ss += s
print(ss)