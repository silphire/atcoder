import math

n, m = map(int, input().split())
aa = list(sorted(map(int, input().split())))

ma = max(m, max(aa))
primes = [True] * (ma + 1)
k = [True] * (ma + 1)
for a in aa:
    k[a] = False
ps = []

for i in range(2, ma + 1):
    if not primes[i]:
        continue
    for j in range(i * 2, ma + 1, i):
        primes[j] = False
        k[i] = k[i] and k[j]
    if not k[i]:
        ps.append(i)

for p in ps:
    for x in range(p * 2, m + 1, p):
        k[x] = k[x] and k[p]

ans = [1]
for i in range(2, m + 1):
    if k[i]:
        ans.append(i)
        
print(len(ans))
for x in ans:
    if x:
        print(x)