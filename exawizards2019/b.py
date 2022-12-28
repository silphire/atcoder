from collections import Counter
n = int(input())
s = input()
ctr = Counter(s)
if ctr['R'] > ctr['B']:
    print('Yes')
else:
    print('No')