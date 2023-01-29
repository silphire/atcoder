s = input()
t = input()

ns = len(s)
nt = len(t)

sf = [None] * (nt + 1)
st = [None] * (nt + 1)
sf[0] = st[0] = True
for i in range(nt):
    st[i + 1] = st[i] and (s[i]      == t[i]      or s[i] == '?'      or t[i] == '?')
    sf[i + 1] = sf[i] and (s[-i - 1] == t[-i - 1] or s[-i - 1] == '?' or t[-i - 1] == '?')
for i in range(nt + 1):
    if st[i] and sf[nt - i]:
        print('Yes')
    else:
        print('No')