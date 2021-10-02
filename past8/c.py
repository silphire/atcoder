from collections import Counter
n, x = map(int, input().split())
aa = list(map(int, input().split()))
print(Counter(aa)[x])
