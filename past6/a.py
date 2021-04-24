s = input().rstrip()
if str.isdecimal(s[:3]) and s[3] == '-' and str.isdecimal(s[4:]):
    print('Yes')
else:
    print('No')