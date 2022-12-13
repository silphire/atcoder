n = int(input())
aa = list(map(int, input().split()))
ai = sorted([i for i in range(n)], key=lambda x: -aa[x])
cc = [0] * n
xx = [None] * n
for i in range(n):
    cc[i] = int(input())
    xx[i] = set(map(int, input().split()))

q = int(input())
for i in range(q):
    d = int(input())
    yy = set(map(int, input().split()))
    f = True
    for a in ai:
        if len(xx[a] & yy) == 0:
            print(a + 1)
            f = False
            break
    if f:
        print(-1)
