n = int(input())
x = tuple(sorted(map(int, input().split())))
y = sum(x[:-1])
if x[-1] < y:
    print('Yes')
else:
    print('No')