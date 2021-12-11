from collections import Counter
n = int(input())
ctr = Counter([input().rstrip() for _ in range(n)])
s = sorted(ctr.items(), key=lambda x: -x[1])
print(s[0][0])
