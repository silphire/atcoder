n = int(input())
aa = list(map(int, input().split()))
q = int(input())
for _ in range(q):
    qq = list(map(int, input().split()))
    if qq[0] == 1:
        aa[qq[1] - 1] = qq[2]
    else:
        print(aa[qq[1] - 1])