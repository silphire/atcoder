s = input()
if set(list(s[1::2])) == {'0'}:
    print('Yes')
else:
    print('No')