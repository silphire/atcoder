s = input().rstrip()
n = len(s)
x = 0
for i, c in enumerate(s):
    if c == 'U':
        x += n - 1 - i + i * 2
    else:
        x += i + (n - 1 - i) * 2
print(x)