n, t, a = map(int, input().split())
if max(t, a) * 2 > n:
    print('Yes')
else:
    print('No')