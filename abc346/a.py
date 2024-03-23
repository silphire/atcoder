n = int(input())
aa = list(map(int, input().split()))

bb = []
for i in range(n - 1):
    bb.append(aa[i] * aa[i + 1])
print(*bb)