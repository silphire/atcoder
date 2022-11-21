n, l = map(int, input().split())
aa = list(map(int, input().split()))

nn = l
np = l
for a in aa:
    if np < 2 and a == 2:
        print('No')
        exit()
    if nn < 1 and a == 1:
        print('No')
        exit()
    nn -= a
    np -= a + 1
print('Yes')