n, k = map(int, input().split())
if k % 2 == 0 and (n - 1) * 2 <= k:
    print('Yes')
else:
    print('No')