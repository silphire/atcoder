q = int(input())
d = {}
for _ in range(q):
    op, *arg = input().split()
    op = int(op)
    if op == 1:
        d[arg[0]] = arg[1]
    else:
        print(d[arg[0]])