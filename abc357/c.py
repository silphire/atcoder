n = int(input())

s = ['#']
while n > 0:
    t = []
    for x in s:
        t.append(x + x + x)
    sp = '.' * len(s[0])
    for x in s:
        t.append(x + sp + x)
    for x in s:
        t.append(x + x + x)
    n -= 1
    s = t
    
for x in s:
    print(x)
