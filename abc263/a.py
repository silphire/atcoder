from collections import Counter
aa = Counter(map(int, input().split()))
if tuple(sorted(aa.values())) == (2, 3):
    print('Yes')
else:
    print('No')