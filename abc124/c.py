s = input().rstrip()
n = len(s)

x1 = 0
x2 = 0
for i in range(n):
    if i % 2 == 0:
        if s[i] == '1':
            x1 += 1
        else:
            x2 += 1
    elif i % 2 == 1:
        if s[i] == '0':
            x1 += 1
        else:
            x2 += 1

print(min(x1, x2))