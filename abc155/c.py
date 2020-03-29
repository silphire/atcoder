from collections import Counter

n = int(input())
ss = []
for _ in range(n):
    ss.append(input().rstrip())
ctr = Counter(ss)

a = sorted([(-v, k) for k, v in ctr.items()])
maxv = a[0][0]
for i in range(len(a)):
    if a[i][0] != maxv:
        break
    print(a[i][1])