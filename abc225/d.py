n, q = map(int, input().split())
f = [0] * (n + 1)
b = [0] * (n + 1)
for _ in range(q):
    qq = list(map(int, input().split()))
    if qq[0] == 1:
        b[qq[1]] = qq[2]
        f[qq[2]] = qq[1]
    elif qq[0] == 2:
        b[qq[1]] = 0
        f[qq[2]] = 0
    else:
        t = qq[1]
        while f[t] != 0:
            t = f[t]
        ans = []
        while t != 0:
            ans.append(t)
            t = b[t]
        print(' '.join(map(str, [len(ans)] + ans)))