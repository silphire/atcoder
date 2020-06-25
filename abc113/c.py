from collections import defaultdict

n, m = map(int, input().split())
yp = []
for i in range(m):
    p, y = map(int, input().split())
    yp.append((y, p, i))
yp = sorted(yp)

code = [0] * m
ctr = defaultdict(int)
for i in range(m):
    ctr[yp[i][1]] += 1
    x = ctr[yp[i][1]]
    code[yp[i][2]] = '{:06}{:06}'.format(yp[i][1], x)
for c in code:
    print(c)