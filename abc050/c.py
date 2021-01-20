from collections import Counter

n = int(input())
aa = list(map(int, input().split()))

ctr = sorted(Counter(aa).items())
f = False
for i, e in enumerate(ctr):
    if i == 0:
        if ctr[0][0] == 0:
            if ctr[0][1] != 1:
                f = True
        elif ctr[0][0] == 1:
            if ctr[0][1] != 2:
                f = True
        else:
            f = True
        if f:
            break
    else:
        if ctr[i][1] == 2:
            if ctr[i][0] != ctr[i - 1][0] + 2:
                f = True
        else:
            f = True
if f:
    print(0)
else:
    ans = 0
    if ctr[0][0] == 0:
        ans = 2 ** (len(ctr) - 1)
    else:
        ans = 2 ** len(ctr)
    ans %= 10 ** 9 + 7
    print(ans)