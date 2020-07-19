s = input().rstrip()

if s[0] != 'A':
    print('WA')
    exit(0)

f = False
for i in range(1, len(s)):
    if s[i] == 'C':
        if i < 2 or i >= len(s) - 1:
            print('WA')
            exit(0)
        if f:
            print('WA')
            exit(0)
        f = True
    elif not str.islower(s[i]):
        print('WA')
        exit(0)

if f:
    print('AC')
else:
    print("WA")
