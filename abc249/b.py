s = input().rstrip()
if len(set(s)) != len(s):
    print('No')
    exit()
fu = False
fl = False
for c in s:
    fu = fu or str.isupper(c)
    fl = fl or str.islower(c)
if fu and fl:
    print('Yes')
else:
    print('No')