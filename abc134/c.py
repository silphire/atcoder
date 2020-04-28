n = int(input())
a = []
for i in range(n):
    a.append((-int(input()), i))
a = sorted(a)
for i in range(n):
    if a[0][1] == i:
        print(-a[1][0])
    else:
        print(-a[0][0])