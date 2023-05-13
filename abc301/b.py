n = int(input())
aa = list(map(int, input().split()))

bb = []
for i in range(n - 1):
    if abs(aa[i] - aa[i + 1]) <= 1:
        bb.append(aa[i])
    elif aa[i] < aa[i + 1]:
        for x in range(aa[i], aa[i + 1]):
            bb.append(x)
    else:
        for x in range(aa[i], aa[i + 1], -1):
            bb.append(x)
bb.append(aa[-1])
print(*bb)