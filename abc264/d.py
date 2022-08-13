s = list(input().rstrip())
t = 'atcoder'
n = len(s)
ans = 0
for i in range(n):
    p = None
    for j in range(i + 1, n):
        if s[j] == t[i]:
            p = j
            break
    if p is None:
        continue
    for j in range(p - 1, i - 1, -1):
        s[j], s[j + 1] = s[j + 1], s[j]
        ans += 1
print(ans)