n = int(input())
aa = list(map(int, input().split()))

total = 0
for i in range(1, n):
    total += abs(aa[i] - aa[i - 1])
total += abs(aa[0]) + abs(aa[-1])

for i in range(n):
    if i == 0:
        print(total - abs(aa[0]) - abs(aa[1] - aa[0]) + abs(aa[1]))
    elif i == n - 1:
        print(total - abs(aa[-1]) + - abs(aa[-1] - aa[-2]) + abs(aa[-2]))
    else:
        print(total - abs(aa[i] - aa[i - 1]) - abs(aa[i + 1] - aa[i]) + abs(aa[i - 1] - aa[i + 1]))
