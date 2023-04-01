n, x = map(int, input().split())
aa = list(map(int, input().split()))

sa = set(aa)
for a in aa:
    if (x + a) in sa:
        print('Yes')
        exit()    
print('No')