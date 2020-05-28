from collections import Counter
s = input().rstrip()
ctr = Counter(s)
if len(ctr) == 2:
    x = min(ctr.values())
else:
    x = 0
print(x * 2)