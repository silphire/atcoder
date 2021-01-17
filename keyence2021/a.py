n = int(input())
aa = tuple(map(int, input().split()))
bb = tuple(map(int, input().split()))

m = 1
x = 1
for i in range(n):
    m = max(m, aa[i])
    x = max(x, m * bb[i])
    print(x)
