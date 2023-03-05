s = input().rstrip()
x = 0
for c in s:
    if c == '(':
        x += 1
    else:
        x -= 1
    if x < 0:
        break
if x == 0:
    print('Yes')
else:
    print('No')