s = input().rstrip()
if not s[0].isupper():
    print('No')
    exit()
if not s[-1].isupper():
    print('No')
    exit()
if not s[1:-1].isdigit():
    print('No')
    exit()
if 100000 <= int(s[1:-1]) <= 999999 and len(s[1:-1]) == 6:
    print('Yes')
else:
    print('No')