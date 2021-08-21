import itertools
s, k = input().split()
ns = len(s)
k = int(k)
a = [i for i in range(len(s))]

ans = set()
for x in sorted(itertools.permutations(s, ns)):
    ans.add(x)
    if len(ans) == k:
        print(''.join(x))
        exit()