n = int(input())
s = input()

for i in range(n - 1):
    x = s[i:i+2]
    if x == 'ab' or x == 'ba':
        print('Yes')
        exit()
print('No')