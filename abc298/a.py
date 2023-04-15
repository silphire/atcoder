from collections import Counter
n = int(input())
s = Counter(list(input()))
if s['o'] > 0 and s['x'] == 0:
    print('Yes')
else:
    print('No')