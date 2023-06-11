from collections import Counter

n = int(input())
x = input()
ss = [
    input()
    for _ in range(n)
]

ctrx = Counter(list(x))

ans = [None] * n
for i in range(n):
    ctrs = Counter(list(ss[i]))
    mc = ''
    cn = 0
    for j in range(26):
        c = chr(ord('A') + j)
        nn = min(2, ctrs[c]) + min(3, ctrx[c])
        if cn < nn:
            mc = c
            cn = nn
    ans[i] = (-cn, mc, i)
print(sorted(ans)[0][2] + 1)