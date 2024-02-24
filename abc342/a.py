from collections import Counter
s = input()
ctr = Counter(list(s))
for c, n in ctr.items():
    if n == 1:
        x = c
for i, c in enumerate(s):
    if c == x:
        print(i + 1)
        exit()