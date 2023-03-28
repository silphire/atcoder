n, k = map(int, input().split())
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))
cc = list(map(int, input().split()))
dd = list(map(int, input().split()))

ab = {a + b for a in aa for b in bb}
cd = {c + d for c in cc for d in dd}
for x in ab:
    if (k - x) in cd:
        print('Yes')
        exit()
print('No')