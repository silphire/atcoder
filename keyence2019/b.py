s = input().rstrip()
n = len(s)
for i in range(n):
    for j in range(i, n):
        if s[:i] + s[j:] == 'keyence':
            print('YES')
            exit()
print('NO')