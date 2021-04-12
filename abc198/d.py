import itertools

s1 = input().rstrip()
s2 = input().rstrip()
s3 = input().rstrip()
ds = {c:i for i, c in enumerate(list(set(s1 + s2 + s3)))}
nd = len(ds)
if nd > 10:
    print('UNSOLVABLE')
    exit()

digits = tuple(map(int, tuple('0123456789')))
for x in itertools.permutations(digits, nd):
    n1 = 0
    n2 = 0
    n3 = 0
    f = False
    for i in range(len(s1)):
        n1 = n1 * 10 + x[ds[s1[i]]]
        if i == 0 and n1 == 0:
            f = True
            break
    if f:
        continue
    for i in range(len(s2)):
        n2 = n2 * 10 + x[ds[s2[i]]]
        if i == 0 and n2 == 0:
            f = True
            break
    if f:
        continue
    for i in range(len(s3)):
        n3 = n3 * 10 + x[ds[s3[i]]]
        if i == 0 and n3 == 0:
            f = True
            break
    if f:
        continue
    if n1 + n2 == n3:
        print(n1)
        print(n2)
        print(n3)
        exit()

print('UNSOLVABLE')
