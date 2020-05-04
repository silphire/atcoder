n = int(input())
s = []
for _ in range(n):
    s.append(list(input().rstrip()))

t = None
for i in range(n - 1, 0, -1):
    t = [list(ss) for ss in s]
    for j in range(2, 2 * n - 1):
        if s[i - 1][j - 1] != '#':
            continue
        if s[i][j - 2] == 'X' or s[i][j - 1] == 'X' or s[i][j] == 'X':
            t[i - 1][j - 1] = 'X'
    s = t

for tt in t:
    print(''.join(tt))