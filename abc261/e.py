n, c = map(int, input().split())
f = [[True] * 2 for _ in range(32)]  # True: same, False: different

for _ in range(n):
    t, a = map(int, input().split())
    for i in range(32):
        b = a & 1
        if t == 1:
            # and
            if b == 0:
                f[i][0] = 0
                f[i][1] = 0
        elif t == 2:
            # or
            if b == 1:
                f[i][0] = 1
                f[i][1] = 1
        else:
            # xor
            if b == 1:
                def reverse(x):
                    if x is True:
                        return False
                    elif x is False:
                        return True
                    elif x == 0:
                        return 1
                    else: # x == 1:
                        return 0
                f[i][0] = reverse(f[i][0])
                f[i][1] = reverse(f[i][1])
        a >>= 1

    nc = 0
    for i in range(32):
        b = c & 1
        if f[i][b] is True:
            nc |= b << i
        elif f[i][b] is False:
            nc |= (1 - b) << i
        else:
            nc |= f[i][b] << i
        c >>= 1
    c = nc
    print(c)
