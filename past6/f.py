n, l, t, x = map(int, input().split())
vt = 0
ans = 0
for i in range(n):
    a, b = map(int, input().split())
    if a > t and b >= l:
        print('forever')
        exit()
    ans += a
    if b < l:
        vt = 0
    else:
        if vt + a == t:
            ans += x
            vt = 0
        elif vt + a > t:
            ans += t - vt + x
            if a == t:
                ans += x
                vt = 0
            else:
                vt = a
        else:
            vt += a
print(ans)