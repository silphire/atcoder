s = input().rstrip()
n = len(s)

ans = 0
for i in range(2 ** (n - 1)):
    sep = []
    for j in range(n):
        if (i >> j) & 1 == 1:
            sep.append(j + 1)
    
    if sep:
        x = int(s[:sep[0]])
    else:
        x = int(s)

    for j in range(len(sep) - 1):
        x += int(s[sep[j] : sep[j + 1]])

    if sep:
        x += int(s[sep[-1]:])

    ans += x

print(ans)