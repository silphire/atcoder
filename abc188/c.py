n = int(input())
aa = list(map(int, input().split()))
for i, x in enumerate(aa):
    aa[i] = (x, i + 1)

for i in range(n - 1):
    for j in range(2 ** (n - i - 1)):
        aa[j] = max(aa[j * 2], aa[j * 2 + 1])
print(min(aa[0], aa[1])[1])