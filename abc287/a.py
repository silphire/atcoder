n = int(input())
x = 0
for i in range(n):
    if input() == 'For':
        x += 1
if x * 2 > n:
    print('Yes')
else:
    print('No')