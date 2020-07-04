from collections import Counter

s = input().rstrip()
t = input().rstrip()

if sorted(Counter(s).values()) == sorted(Counter(t).values()):
    print('Yes')
else:
    print('No')