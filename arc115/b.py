n = int(input())
cc = [
    list(map(int, input().split()))
    for _ in range(n)
]

aa = [0] * n
bb = [0] * n

p = 0
ma = float('inf')
for i in range(n):
    if cc[i][0] < ma:
        ma = cc[i][0]
        p = i

for i in range(n):
    aa[i] = cc[i][0] - ma

for i in range(n):
    bb[i] = cc[p][i]

for i in range(n):
    for j in range(n):
        if aa[i] + bb[j] != cc[i][j]:
            print('No')
            exit()
print('Yes')
print(*aa)
print(*bb)