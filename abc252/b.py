n, k = map(int, input().split())
aa = list(map(int, input().split()))
bb = set(map(int, input().split()))

m = max(aa)
ms = {i + 1 for i, a in enumerate(aa) if a == m}
if len(bb & ms) > 0:
    print('Yes')
else:
    print('No')