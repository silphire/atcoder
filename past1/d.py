from collections import Counter

n = int(input())
aa = []
for _ in range(n):
    aa.append(int(input()))

ctr = Counter(aa)
if set(ctr.values()) == {1}:
    print("Correct")
    exit(0)

miss = None
dupl = None
for i in range(1, n + 1):
    if i not in ctr:
        miss = i
    elif ctr[i] == 2:
        dupl = i
print("{} {}".format(dupl, miss))