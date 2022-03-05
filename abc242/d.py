tb = {'A': 'BC', 'B': 'CA', 'C': 'AB'}

s = input().rstrip()
q = int(input())
for _ in range(q):
    ss = s
    t, k = map(int, input().split())
    k -= 1

    nk = 0
    kk = k
    while kk > 0:
        nk += 1
        kk >>= 1
    if t > nk:
        ss = chr(ord('A') + (ord(s[0]) - ord('A') + t - nk) % 3)
        t = nk - 1
    else:
        ss = s[k >> t]
        t -= 1
    while t >= 0:
        ss = tb[ss][(k >> t) & 1]
        t -= 1
    print(ss)