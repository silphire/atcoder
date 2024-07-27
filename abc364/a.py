n = int(input())
r = ''
for i in range(n):
    s = input()
    if s == r == 'sweet' and i + 1 < n:
        print('No')
        exit()
    r = s
print('Yes')