from collections import defaultdict

n = int(input())
ss = [None] * n
tt = [None] * n
ctr = defaultdict(int)

for i in range(n):
    ss[i], tt[i] = input().rstrip().split()
    ctr[ss[i]] += 1
    ctr[tt[i]] += 1

for i in range(n):
    if ss[i] == tt[i] and ctr[ss[i]] == 2:
        continue
    if ctr[ss[i]] == 1 or ctr[tt[i]] == 1:
        continue
    print('No')
    exit()
print('Yes')