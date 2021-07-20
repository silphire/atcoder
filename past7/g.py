n = int(input())
nn = n
dd = []
while nn > 0:
    dd.append(nn % 3)
    nn //= 3
dd.append(0)
ans = []
x = 1
for i, d in enumerate(dd):
    if d >= 3:
        dd[i + 1] += d // 3
        d %= 3
    if d == 1:
        ans.append(x)
    elif d == 2:
        ans.append(-x)
        dd[i + 1] += 1
    x *= 3
print(len(ans))
print(' '.join(map(str, ans)))