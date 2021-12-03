s = input().rstrip()
t = 'oxx'
for i in range(3):
    f = True
    for j in range(len(s)):
        if s[j] != t[(i + j) % 3]:
            f = False
            break
    if f:
        print('Yes')
        exit()
print('No')