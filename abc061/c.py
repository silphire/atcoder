from collections import Counter

n, k = map(int, input().split())
ctr = Counter()

for i in range(n):
    a, b = map(int, input().split())
    ctr[a] += b
for num, c in sorted(ctr.items()):
    k -= c
    if k <= 0:
        print(num)
        exit()