s = input()
t = ''
for c in s:
    if c == '0':
        t += '1'
    else:
        t += '0'
print(t)