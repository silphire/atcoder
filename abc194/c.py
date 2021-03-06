from collections import Counter
n = int(input())
aa = list(map(int, input().split()))

tb = [[(a - b) ** 2 for a in range(-200, 201)] for b in range(-200, 201)]
ans = 0
aa = list(Counter(aa).items())
for i in range(len(aa)):
    for j in range(i + 1, len(aa)):
        ans += tb[aa[i][0] + 200][aa[j][0] + 200] * aa[i][1] * aa[j][1]
print(ans)