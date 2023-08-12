n = int(input())
d = [list() for _ in range(37)]
for i in range(n):
    c = int(input())
    aa = list(map(int, input().split()))
    for a in aa:
        d[a].append((c, i + 1))

x = int(input())
d[x].sort()
ans = []
if len(d[x]) > 0:
    for i in range(len(d[x])):
        if d[x][i][0] == d[x][0][0]:
            ans.append(d[x][i][1])
        else:
            break

print(len(ans))
print(*sorted(ans))