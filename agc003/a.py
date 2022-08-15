s = set(input().rstrip())
if ('N' in s) == ('S' in s) and ('W' in s) == ('E' in s):
    print('Yes')
else:
    print('No')