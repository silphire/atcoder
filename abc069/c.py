n = int(input())
aa = list(map(int, input().split()))

n2 = 0
n4 = 0
for a in aa:
    if a % 4 == 0:
        n4 += 1
    elif a % 2 == 0:
        n2 += 1

n -= n2 // 2 * 2
if n // 2 <= n4:
    print('Yes')
else:
    print('No')