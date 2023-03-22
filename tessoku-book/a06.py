n, q = map(int, input().split())
aa = list(map(int, input().split()))
acc = [0] * (n + 1)
acc[0] = aa[0]
for i in range(n):
    acc[i + 1] = acc[i] + aa[i]

for _ in range(q):
    l, r = map(int, input().split())
    print(acc[r] - acc[l - 1])