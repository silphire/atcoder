s = list(input().rstrip())
n = len(s)
x = 0
b = 0
for i in range(n):
    if s[i] == 'B':
        b += 1
    else:
        x += b
print(x)