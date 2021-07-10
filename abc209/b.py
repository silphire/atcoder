n, x = map(int, input().split())
aa = list(map(int, input().split()))

ans = x - sum(aa) + n // 2
if ans >= 0:
    print('Yes')
else:
    print('No')