n = int(input())
aa = list(map(int, input().split()))
ff = [0] * n

q = int(input())
x = 0
w = -1
for i in range(q):
    qq = list(map(int, input().split()))
    if qq[0] == 1:
        w = i
        x = qq[1]
    elif qq[0] == 2:
        qi = qq[1] - 1
        if ff[qi] <= w:
            aa[qi] = x
        aa[qi] += qq[2]
        ff[qi] = i
    else:
        qi = qq[1] - 1
        if ff[qi] <= w:
            ff[qi] = i
            aa[qi] = x
        print(aa[qi])
