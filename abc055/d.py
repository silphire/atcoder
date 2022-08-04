n = int(input())
s = input().rstrip()

for pt in range(4):
    t = [None] * n
    for i in range(2):
        t[i - 1] = (pt >> i) & 1

    for i in range(n - 1):
        if t[i] == 0:
            if s[i] == 'o':
                nt = t[i - 1]
            else:
                nt = 1 - t[i - 1]
        else:
            if s[i] == 'x':
                nt = t[i - 1]
            else:
                nt = 1 - t[i - 1]
        if t[i + 1] is None:
            t[i + 1] = nt
        elif t[i + 1] == nt:
            if t[-1] == 0:
                if s[-1] == 'o':
                    f = t[-2] == t[0]
                else:
                    f = t[-2] != t[0]
            else:
                if s[-1] == 'x':
                    f = t[-2] == t[0]
                else:
                    f = t[-2] != t[0]
            if f:
                print(''.join(map(lambda x: 'SW'[x], t)))
                exit()
print(-1)