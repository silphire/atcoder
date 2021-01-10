n = int(input())
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))

x = 0
for i in range(n):
    x += aa[i] * bb[i]
if x == 0:
    print('Yes')
else:
    print('No')