s = input().rstrip()
n = len(s)
x = ''
d = 0
for i in range(n - 1, -1, -1):
    if s[i] == 'B':
        d += 1
    else:
        if d > 0:
            d -= 1
        else:
            x = s[i] + x
print(x)
