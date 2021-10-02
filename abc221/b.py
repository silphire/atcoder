s = list(input().rstrip())
t = list(input().rstrip())

n = len(s)
x = 0
for i in range(n):
    if s[i] != t[i]:
        if i + 1 < n:
            s[i], s[i + 1] = s[i + 1], s[i]
            break
if tuple(s) == tuple(t):
    print('Yes')
else:
    print('No')