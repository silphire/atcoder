from collections import Counter

n, k = map(int, input().split())
ctr = Counter(map(int, input().split()))

aa = sorted(ctr.items(), key=lambda x: x[1])
if len(aa) <= k:
    print(0)
else:
    print(sum(map(lambda x: x[1], aa[:len(aa) - k])))
