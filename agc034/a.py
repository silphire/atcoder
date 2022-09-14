n, a, b, c, d = map(int, input().split())
a -= 1
b -= 1
c -= 1
d -= 1
s = input().rstrip()

for x, y in ((a, c), (b, d)):
    for i in range(x + 1, y + 1):
        if s[i - 1] == '#' and s[i] == '#':
            print('No')
            exit()
if c > d:
    for i in range(b, d + 1):
        if i - 1 < 0 or i + 1 >= n:
            continue
        if s[i - 1] == '.' and s[i] == '.' and s[i + 1] == '.':
            print('Yes')
            exit()
    print('No')
else:
    print('Yes')