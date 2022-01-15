n = int(input())
hh = list(map(int, input().split()))
for i in range(n - 1):
    if hh[i] >= hh[i + 1]:
        print(hh[i])
        exit()
print(hh[-1])