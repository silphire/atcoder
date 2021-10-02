n = int(input())
s = input().rstrip()

sn = None
pn = None
ans = [0] * n
for i in range(n):
    if s[i] == '1':
        ans[i] = i + 1
    else:
        if pn is None:
            sn = i
        else:
            ans[pn] = i + 1
        pn = i
if sn is not None:
    if sn == pn:
        print(-1)
        exit()
    ans[pn] = sn + 1
print(' '.join(map(str, ans)))