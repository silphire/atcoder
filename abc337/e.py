num = n = int(input())

m = 0
while num > 1:
    m += 1
    num //= 2
if 1 << m != n:
    m += 1
print(m)

aa = [[] for _ in range(m)]
for i in range(1, n + 1):
    for j in range(m):
        if (i >> j) & 1 == 1:
            aa[j].append(i)

for a in aa:
    print(*([len(a)] + a))

s = input()

ans = set([i + 1 for i in range(n)])
for i, c in enumerate(s):
    if c == '0':
        ans -= set(aa[i])
    else:
        ans = ans & set(aa[i])
print(list(ans)[0])