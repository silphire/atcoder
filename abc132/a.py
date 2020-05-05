from collections import Counter
c = Counter(input().rstrip())
if len(c) == 2 and list(set(c.values()))[0] == 2:
    print('Yes')
else:
    print('No')