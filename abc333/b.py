s = input()
t = input()
sd = abs(ord(s[0]) - ord(s[1]))
td = abs(ord(t[0]) - ord(t[1]))
sd = min(abs(sd), abs(5 - sd))
td = min(abs(td), abs(5 - td))
if sd == td:
    print('Yes')
else:
    print('No')