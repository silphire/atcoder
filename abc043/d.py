s = input().rstrip()

if s[0] == s[1]:
    print('1 2')
    exit()

for i in range(2, len(s)):
    if s[i] == s[i - 1]:
        print(f'{i} {i + 1}')
        exit()
    if s[i] == s[i - 2]:
        print(f'{i - 1} {i + 1}')
        exit()
print('-1 -1')