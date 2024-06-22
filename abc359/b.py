n = int(input())
aa = list(map(int, input().split()))

x = 0
for i in range(2 * n - 2):
    if aa[i] == aa[i + 2]:
        x += 1
print(x)