n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = list(input().rstrip())

tb = {'r': p, 's': r, 'p': s}
ans = 0
for i in range(len(t)):
    if i < k:
        ans += tb[t[i]]
    else:
        if t[i - k] == t[i]:
            t[i] = '-'
        else:
            ans += tb[t[i]]
print(ans)
