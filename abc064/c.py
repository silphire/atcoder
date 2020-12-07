from collections import defaultdict

n = int(input())
aa = list(map(int, input().split()))

f = 0
c = defaultdict(int)

for i in range(n):
    if aa[i] >= 3200:
        f += 1
    else:
        c[aa[i] // 400] += 1
c = len(c)

minc = max(1, c)
maxc = c + f
print(f'{minc} {maxc}')