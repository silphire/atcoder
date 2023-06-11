from collections import Counter

h, w = map(int, input().split())
ss = [
    Counter(list(input()))['#']
    for _ in range(h)
]
tt = [
    Counter(list(input()))['#']
    for _ in range(h)
]

if ss == tt:
    print('Yes')
else:
    print('No')