s = input().upper()
t = input()

n = 0
for c in s:
    if t[n] == c:
        n += 1
        if n > 3:
            print('No')
            exit()
        elif n == 2 and t[-1] == 'X':
            print('Yes')
            exit()
        elif n == 3:
            print('Yes')
            exit()
print('No')