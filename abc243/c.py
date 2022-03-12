from collections import defaultdict

n = int(input())
xx = [0] * n
yy = [0] * n
for i in range(n):
    xx[i], yy[i] = map(int, input().split())
s = input().rstrip()

d = defaultdict(list)
for i in range(n):
    if s[i] == 'L':
        sg = -1
    else:
        sg = 1
    d[yy[i]].append((xx[i], sg))

ys = set(yy)
for y in ys:
    d[y].sort()
    ps = -100
    for x, sg in d[y]:
        if ps > sg:
            print('Yes')
            exit()
        ps = sg
print('No')
