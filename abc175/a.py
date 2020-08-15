s = input().rstrip()
x = 0
for i in range(len(s)):
    if s[i] == 'R':
        x += 1
    elif x > 0:
        print(x)
        exit(0)
print(x)
