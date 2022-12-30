from collections import Counter
s = input()
c = Counter(s)
if 15 - len(s) + c['o'] >= 8:
    print('YES')
else:
    print('NO')