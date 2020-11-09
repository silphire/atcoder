from collections import Counter

n = int(input())
ctr = sorted(Counter(map(int, input().split())).items())
ans = 0
if len(ctr) == 1:
    print(ctr[0][1])
elif len(ctr) == 2:
    if ctr[0][0] + 1 == ctr[1][0]:
        print(ctr[0][1] + ctr[1][1])
    else:
        print(max(ctr[0][1], ctr[1][1]))
else:
    for i in range(len(ctr) - 2):
        if ctr[i][0] + 1 == ctr[i + 1][0] and ctr[i][0] + 2 == ctr[i + 2][0]:
            ans = max(ans, ctr[i][1] + ctr[i + 1][1] + ctr[i + 2][1])
    print(ans)
