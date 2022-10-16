from collections import Counter
aa = []
for i in range(3):
    aa += map(int, input().split())
ctr = Counter(aa)
ctr2 = Counter(ctr.values())
if ctr2[1] == 2 and ctr2[2] == 2:
    print('YES')
else:
    print('NO')