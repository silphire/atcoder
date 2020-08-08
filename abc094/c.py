n = int(input())
x = list(map(int, input().split()))

y = sorted([(a, i) for i, a in enumerate(x)])
x1 = y[n // 2 - 1][0]
x2 = y[n // 2][0]

for i in range(n):
    j = y[i][1]
    x[j] = (x[j], i)

for i in range(n):
    if x[i][1] < n // 2:
        print(x2)
    else:
        print(x1)