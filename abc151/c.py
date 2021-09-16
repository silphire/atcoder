n, m = map(int, input().split())
p = []
s = []
for i in range(m):
    pp, ss = input().split()
    p.append(int(pp) - 1)
    s.append(ss)

acs = [0] * n
was = [0] * n
for i in range(m):
    if s[i] == 'AC':
        acs[p[i]] = 1
    else:
        if acs[p[i]] == 0:
            was[p[i]] += 1
for i in range(n):
    if acs[i] == 0:
        was[i] = 0
print("{} {}".format(sum(acs), sum(was)))
