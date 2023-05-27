n = int(input())
s = input()
t = input()

for i in range(n):
    x = s[i]
    y = t[i]
    if x == y or x == '1' and y == 'l' or x == 'l' and y == '1' or x == '0' and y == 'o' or x == 'o' and y == '0':
        pass
    else:
        print('No')
        exit()
print('Yes')