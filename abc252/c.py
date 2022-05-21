from collections import defaultdict

n = int(input())
ss = [
    input().rstrip()
    for _ in range(n)
]

pos = [[] for _ in range(10)]
for i in range(10):
    for j in range(n):
        x = int(ss[j][i])
        pos[x].append(i)
ans = float('inf')
for i in range(10):
    pos[i].sort()
    for j in range(1, len(pos[i])):
        if pos[i][j] == pos[i][j - 1] % 10:
            pos[i][j] = pos[i][j - 1] + 10
    ans = min(ans, max(pos[i]))
print(ans)