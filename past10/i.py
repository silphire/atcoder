n = int(input())
ss = sorted([
    tuple(map(int, input().split()))
    for _ in range(n)
])
tt = sorted([
    tuple(map(int, input().split()))
    for _ in range(n)
])

if ss == tt:
    print('Yes')
    exit()

ss = sorted(ss, key=lambda p: (p[0], p[1]))
tt = sorted(tt, key=lambda p: (-p[0], p[1]))

f = True
x = ss[0][0] + tt[0][0]
for i in range(n):
    if not(ss[i][1] == tt[i][1] and ss[i][0] + tt[i][0] == x):
        f = False
        break
if f:
    print('Yes')
    exit()

ss = sorted(ss, key=lambda p: (p[1], p[0]))
tt = sorted(tt, key=lambda p: (-p[1], p[0]))

f = True
y = ss[0][1] + tt[0][1]
for i in range(n):
    if not(ss[i][0] == tt[i][0] and ss[i][1] + tt[i][1] == y):
        f = False
        break

if f:
    print('Yes')
else:
    print('No')