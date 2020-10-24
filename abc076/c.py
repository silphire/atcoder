s = list(input().rstrip())
t = list(input().rstrip())

ans = []
for i in range(len(s) - len(t) + 1):
    f = False
    for j in range(len(t)):
        if s[i + j] == '?' or s[i + j] == t[j]:
            continue
        f = True
        break
    if f:
        continue
    ss = ['?' for _ in range(len(s))]
    for j in range(len(t)):
        ss[i + j] = t[j]
    for j in range(len(s)):
        if ss[j] == '?':
            if s[j] == '?':
                ss[j] = 'a'
            else:
                ss[j] = s[j]
    ans.append(''.join(ss))

if ans:
    print(sorted(ans)[0])
else:
    print('UNRESTORABLE')
