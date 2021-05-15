s = input().rstrip()
so = set()
sx = set()
for i in range(10):
    if s[i] == 'o':
        so.add(i)
    elif s[i] == 'x':
        sx.add(i)
ans = 0
for x in range(10000):
    sd = set()
    for i in range(4):
        d = x % 10
        sd.add(d)
        x //= 10
    if len(so - sd) == 0 and len(sx - sd) == len(sx):
        ans += 1 
print(ans)