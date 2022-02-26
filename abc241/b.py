from collections import Counter

n, m = map(int, input().split())
aa = Counter(map(int, input().split()))
bb = Counter(map(int, input().split()))

for b, x in bb.items():
    if aa[b] < x:
        print('No')
        exit()
print('Yes')
