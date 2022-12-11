r, n, m, l = map(int, input().split())
ss = list(map(int, input().split()))

p = 0
for _ in range(r):
    nr = n
    for i in range(m):
        if p == l:
            print('No')
            exit()
        nr -= ss[p]
        p += 1
        if nr == 0:
            break
        elif nr < 0:
            print('No')
            exit()
if p == l:
    print('Yes')
else:
    print('No')