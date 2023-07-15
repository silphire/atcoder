n = int(input())
ss = [
    input()
    for _ in range(n)
]

sp = set()
sn = set()
np = 0
nn = 0
for s in ss:
    r = s[::-1]
    if s == r:
        np += 1
        sp.add(s)
    else:
        nn += 1
        sn.add(s)
        sn.add(r)
print(len(sp) + len(sn) // 2)
