from collections import Counter
n = int(input())
aa = list(map(int, input().split()))

if set(aa) == {0}:
    print('Yes')
    exit()
elif len(aa) % 3 != 0:
    print('No')
    exit()

ctr = Counter(aa)
if len(ctr) == 2 and ctr[0] == n // 3 and ctr.most_common()[0][1] == 2 * n // 3:
    print('Yes')
    exit()
elif len(ctr) == 3:
    mc = ctr.most_common()
    if mc[0][0] ^ mc[1][0] ^ mc[2][0] == 0 and mc[0][1] == mc[1][1] == mc[2][1] == n // 3:
        print('Yes')
        exit()
print('No')