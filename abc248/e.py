n, k = map(int, input().split())
xx = [0] * n
yy = [0] * n
for i in range(n):
    xx[i], yy[i] = map(int, input().split())

if k == 1:
    print('Infinity')
    exit()

ans = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            pass

print(ans)