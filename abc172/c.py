n, m, k = map(int, input().split())
aa = [0] + list(map(int, input().split()))
bb = [0] + list(map(int, input().split()))
n += 1
m += 1

for i in range(1, n):
    aa[i] += aa[i - 1]
for i in range(1, m):
    bb[i] += bb[i - 1]

ans = 0
b = m - 1
for a in range(n):
    while b >= 0 and aa[a] + bb[b] > k:
        b -= 1
    if b >= 0:
        ans = max(ans, a + b)
print(ans)