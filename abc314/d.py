n = int(input())
s = list(input())
fl = None
org = set()
    
q = int(input())
for _ in range(q):
    t, x, c = input().split()
    t = int(t)
    x = int(x)
    if t == 1:
        s[x - 1] = c
        org.add(x - 1)
    elif t == 2:
        org = set()
        fl = True
    else:
        org = set()
        fl = False

if fl is not None:
    for i, c in enumerate(s):
        if i in org:
            continue
        if fl:
            s[i] = c.lower()
        else:
            s[i] = c.upper()
print(''.join(s))