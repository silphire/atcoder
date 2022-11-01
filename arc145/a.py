n = int(input())
s = input().rstrip()
if s == 'BA':
    print('No')
elif s[0] == 'A' and s[-1] == 'B':
    print('No')
else:
    print('Yes')