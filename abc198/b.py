n = input().rstrip()
z = 0
for i in range(len(n)):
    if n[-i - 1] == '0':
        z += 1
    else:
        break
n = ('0' * z) + n
m = str(''.join(list(reversed(n))))
if n == m:
    print('Yes')
else:
    print('No')