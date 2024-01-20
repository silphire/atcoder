import re

s = input()
if re.fullmatch('A*B*C*', s):
    print('Yes')
else:
    print('No')