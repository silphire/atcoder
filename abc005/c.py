t = int(input())
n = int(input())
aa = list(map(int, input().split()))
m = int(input())
bb = list(map(int, input().split()))

if n < m:
    print('no')
    exit()

aa.sort()
bb.sort()

b = 0
for a in aa:
    if bb[b] < a:
        print('no')
        exit()
    elif bb[b] <= a + t:
        b += 1
    if b == m:
        print('yes')
        exit()
print('no')