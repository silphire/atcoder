import itertools

n = int(input())
aa = []
for i in range(1, n):
    aa.append([0] * i + list(map(int, input().split())))

for i in range(n):
    for j in range(i + 1, n - 1):
        aa[j][i] = aa[i][j]

ans = -100000000
for i in range(3 ** n):
    members = [[], [], []]
    x = i
    for j in range(n):
        members[x % 3].append(j)
        x //= 3
    
    r = 0
    for t in range(3):
        for c in itertools.combinations(members[t], 2):
            r += aa[c[0]][c[1]]
    ans = max(ans, r)

print(ans)