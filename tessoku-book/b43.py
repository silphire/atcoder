from collections import Counter
n, m = map(int, input().split())
ctr = Counter(map(int, input().split()))
for i in range(n):
    print(m - ctr[i + 1])