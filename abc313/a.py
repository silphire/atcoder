from collections import Counter

n = int(input())
pp = list(map(int, input().split()))
ctr = Counter(pp)

if max(pp) == pp[0]:
    if ctr[pp[0]] == 1:
        print(0)
    else:
        print(1)
else:
    print(max(pp) - pp[0] + 1)