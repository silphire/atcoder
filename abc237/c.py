s = input().rstrip()
n = len(s)

al = 0
ar = 0
for i in range(n):
    if s[i] == 'a':
        al += 1
    else:
        break
for i in range(n):
    if s[n - 1 - i] == 'a':
        ar += 1
    else:
        break
s = ('a' * max(0, ar - al)) + s

n = len(s)
for i in range(n // 2):
    if s[i] != s[n - 1 - i]:
        print('No')
        exit()
print('Yes')