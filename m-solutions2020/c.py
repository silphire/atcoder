n, k = map(int, input().split())
aa = tuple(map(int, input().split()))

for i in range(k, n):
    if aa[i - k] < aa[i]:
        print('Yes')
    else:
        print('No')
