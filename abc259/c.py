s = input().rstrip()
t = input().rstrip()

ss = []
for i in range(len(s)):
    if i == 0 or s[i] != s[i - 1]:
        ss.append((s[i], 1))
    else:
        ss[-1] = (ss[-1][0], ss[-1][1] + 1)
tt = []
for i in range(len(t)):
    if i == 0 or t[i] != t[i - 1]:
        tt.append((t[i], 1))
    else:
        tt[-1] = (tt[-1][0], tt[-1][1] + 1)
if len(ss) != len(tt):
    print('No')
else:
    for s, t in zip(ss, tt):
        if s[0] != t[0]:
            print('No')
            exit()
        if s[1] != t[1]:
            if not (1 < s[1] < t[1]):
                print('No')
                exit()
                
    print('Yes')