from collections import Counter
n = int(input())
s = input()

mball = max(map(lambda x: len(x), s.split('-')))
ctr = Counter(list(s))
if ctr['o'] > 0 and ctr['-'] > 0:
    print(mball)
else:
    print(-1)