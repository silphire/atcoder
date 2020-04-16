n, m = map(int, input().split())
ss = []
for i in range(m):
    s = list(map(int, input().split()))
    x = 0
    for i in range(1, len(s)):
        x |= 1 << (s[i] - 1)
    ss.append(x)
pp = list(map(int, input().split()))

ans = 0
for x in range(2 ** n):
    non = 0
    for i in range(m):
        a = ss[i] & x
        nb = 0
        while a != 0:
            if a & 1 == 1:
                nb += 1
            a >>= 1
        if nb % 2 == pp[i]:
            non += 1
    if non == m:
        ans += 1
print(ans)