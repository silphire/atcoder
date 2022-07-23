from collections import defaultdict

n = int(input())
ctr = defaultdict(int)
for i in range(n):
    s = input().rstrip()
    if s in ctr:
        print(f'{s}({ctr[s]})')
    else:
        print(s)
    ctr[s] += 1
