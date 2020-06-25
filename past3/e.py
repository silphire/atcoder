n, m, q = map(int, input().split())

e = [set() for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    e[u].add(v)
    e[v].add(u)

c = list(map(int, input().split()))

for i in range(q):
    s = tuple(map(int, input().split()))
    vv = s[1] - 1
    print(c[vv])
    if s[0] == 1:
        for ee in e[vv]:
            c[ee] = c[vv]
    else:
        c[vv] = s[2]

