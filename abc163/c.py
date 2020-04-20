from collections import Counter

n = int(input())
aa = list(map(int, input().split()))
ctr = Counter(aa)
for i in range(len(aa) + 1):
    if i + 1 in ctr:
        print(ctr[i + 1])
    else:
        print(0)