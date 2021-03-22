n = int(input())
ms = ''
mp = 0
all = 0
for i in range(n):
    s, p = input().rstrip().split()
    p = int(p)
    if mp < p:
        ms = s
        mp = p
    all += p
if mp * 2 > all:
    print(ms)
else:
    print('atcoder')