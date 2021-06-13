n = int(input())
aa = list(map(int, input().split()))

aa.sort()
for i, a in enumerate(aa):
    if a != i + 1:
        print('No')
        exit()
print('Yes')