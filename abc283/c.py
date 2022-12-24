s = input()
x = 0
i = 0
while i < len(s):
    x += 1
    if s[i:i+2] == '00':
        i += 2
    else:
        i += 1
print(x)