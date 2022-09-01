n = int(input())
ss = [
    input().rstrip()
    for _ in range(n)
]

ans = 0
na = 0
nb = 0
nab = 0
for s in ss:
    for i in range(len(s) - 1):
        if s[i:i+2] == 'AB':
            ans += 1
    fb = s[0] == 'B'
    fa = s[-1] == 'A'
    if fa and fb:
        nab += 1
    elif fa:
        na += 1
    elif fb:
        nb += 1

if nab == 0:
    ans += min(na, nb)
else:
    if na + nb > 0:
        ans += nab + min(na, nb)
    elif na + nb == 0:
        ans += nab - 1
print(ans)