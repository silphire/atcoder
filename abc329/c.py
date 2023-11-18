from collections import defaultdict
n = int(input())
s = input()
x = 0
p = None
d = defaultdict(int)
for c in s:
    if p != c:
        if p is not None:
            d[p] = max(d[p], x)
        p = c
        x = 0
    x += 1
d[p] = max(d[p], x)
print(sum(d.values()))