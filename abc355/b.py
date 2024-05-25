n, m = map(int, input().split())
aa = list(map(lambda x: (int(x), 0), input().split()))
bb = list(map(lambda x: (int(x), 1), input().split()))
cc = sorted(aa + bb)
for i in range(1, len(cc)):
    if cc[i - 1][1] == cc[i][1] == 0:
        print('Yes')
        exit()
print('No')