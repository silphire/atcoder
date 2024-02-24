n = int(input())
s = input()

q = int(input())
cc = [0] * q
dd = [0] * q
for i in range(q):
    cc[i], dd[i] = input().split()

tb = {}
for i in range(q - 1, -1, -1):
    c = cc[i]
    d = dd[i]
    if d in tb:
        tb[c] = tb[d]
    else:
        tb[c] = d

t = [None] * n
for i, c in enumerate(s):
    t[i] = tb.get(c, c)
print(''.join(t))