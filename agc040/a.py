s = input().rstrip()
n = len(s)
ll = [0] * (n + 1)
rr = [0] * (n + 1)

x = 0
for i in range(n):
    if s[i] == '<':
        x += 1
    else:
        x = 0
    ll[i + 1] = x

x = 0
for i in range(n - 1, -1, -1):
    if s[i] == '>':
        x += 1
    else:
        x = 0
    rr[i] = x

x = 0
for i in range(n + 1):
    x += max(ll[i], rr[i])
print(x)
