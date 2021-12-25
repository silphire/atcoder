from collections import Counter
n, k = map(int, input().split())
aa = list(map(int, input().split()))
for i in range(1, n):
    aa[i] += aa[i - 1]
aa = [0] + aa
n += 1

ctr = Counter([0])
x = 0
ans = 0
for i in range(1, n):
    ans += ctr[aa[i] - k]
    ctr[aa[i]] += 1
print(ans)