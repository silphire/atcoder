n, p, q, r = map(int, input().split())
aa = list(map(int, input().split()))

ac = [0] * (n + 1)
for i, a in enumerate(aa):
    ac[i + 1] = ac[i] + a
ss = {}
for i, a in enumerate(ac):
    ss[a] = i

for a in ac:
    if (a + p) in ss and (a + p + q) in ss and (a + p + q + r) in ss and (ss[a] < ss[a + p] < ss[a + p + q] < ss[a + p + q + r]):
        print('Yes')
        exit()
print('No')