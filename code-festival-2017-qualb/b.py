from collections import Counter

n = int(input())
dd = list(map(int, input().split()))
m = int(input())
tt = list(map(int, input().split()))

ctr = Counter(dd)
if all([ctr[t] >= n for t, n in Counter(tt).items()]):
    print('YES')
else:
    print('NO')