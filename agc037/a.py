s = input().rstrip()
n = len(s)

ans = 0
ss = [s[0]]
x = ''
for i in range(1, n):
    x += s[i]
    if x != ss[-1]:
        ss.append(x)
        x = ''
print(len(ss))