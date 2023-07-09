n = int(input())
aa = [
    list(map(int, input().split()))
    for _ in range(n)
]

tb = [i for i in range(n)]
q = int(input())
for _ in range(q):
    op, y, x = map(int, input().split())
    x -= 1
    y -= 1
    if op == 1:
        tb[x], tb[y] = tb[y], tb[x]
    else:
        print(aa[tb[y]][x])
