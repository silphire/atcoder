n = int(input())
aa = list(map(int, input().split()))
ans = [0] * (2 ** n)

for i, a in enumerate(aa):
    aa[i] = (a, i)

nb = 1
while len(aa) > 1:
    bb = [None] * (len(aa) // 2)
    for i in range(len(bb)):
        bb[i] = max(aa[i * 2], aa[i * 2 + 1])
        loser = min(aa[i * 2], aa[i * 2 + 1])[1]
        ans[loser] = nb
    nb += 1
    aa = bb
ans[aa[0][1]] = nb - 1

for a in ans:
    print(a)