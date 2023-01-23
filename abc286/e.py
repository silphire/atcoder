n = int(input())
aa = list(map(int, input().split()))
ss = [
    input()
    for _ in range(n)
]

inf = 1 << 60
d = [
    [(inf, 0) for _ in range(n)]
    for _ in range(n)
]
for i in range(n):
    for j in range(n):
        if ss[i][j] == 'Y':
            d[i][j] = (1, -aa[j])
        

for k in range(n):
    for i in range(n):
        for j in range(n):
            d1 = d[i][j]
            d2 = (d[i][k][0] + d[k][j][0], d[i][k][1] + d[k][j][1])
            if d1 > d2:
                d[i][j] = d2

q = int(input())
for i in range(q):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if d[u][v][0] == inf:
        print('Impossible')
    else:
        print(d[u][v][0], -d[u][v][1] + aa[u])