s = input().rstrip()
if ''.join(sorted(s)) == 'abc':
    print('Yes')
else:
    print('No')