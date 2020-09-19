n = int(input())
d = [
    list(map(int, input().split()))
    for _ in range(n)
]

c = 0
maxc = 0
for i in range(n):
    if d[i][0] == d[i][1]:
        c += 1
        maxc = max(maxc, c)
    else:
        c = 0
if maxc >= 3:
    print('Yes')
else:
    print('No')