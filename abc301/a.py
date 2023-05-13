from collections import Counter
n = int(input())
s = input()
ctr = Counter(list(s))
if ctr['T'] > ctr['A']:
    print('T')
elif ctr['A'] > ctr['T']:
    print('A')
else:
    if s[-1] == 'T':
        print('A')
    else:
        print('T')