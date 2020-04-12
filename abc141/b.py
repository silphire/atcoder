s = input().rstrip()

odd = 'RUD'
even = 'LUD'

for i in range(len(s)):
    if i % 2 == 0:
        if s[i] not in odd:
            print('No')
            exit(0)
    else:
        if s[i] not in even:
            print('No')
            exit(0)
print('Yes')