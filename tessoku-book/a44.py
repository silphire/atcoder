n, q = map(int, input().split())
f = True
aa = [i + 1 for i in range(n)]
for _ in range(q):
    op, *arg = map(int, input().split())
    if op == 1:
        if f:
            aa[arg[0] - 1] = arg[1]
        else:
            aa[n - arg[0]] = arg[1]
    elif op == 2:
        f = not f
    else:
        if f:
            print(aa[arg[0] - 1])
        else:
            print(aa[n - arg[0]])