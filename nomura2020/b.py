t = input().rstrip()

s = ''
f = False
for i, tt in enumerate(t):
    if f:
        f = False
        continue
    if t[i] == '?':
        s += 'D'
    else:
        s += tt
print(s)