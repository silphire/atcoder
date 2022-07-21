n = int(input())
pp = sorted([tuple(map(lambda x: int(x[:2]) * 60 + int(x[2:]), input().rstrip().split('-'))) for i in range(n)])

for i in range(n):
    pp[i] = (
        pp[i][0] // 5 * 5,
        (pp[i][1] // 5 + int(pp[i][1] % 5 != 0)) * 5,
    )

aa = [pp[0]]
for i in range(1, n):
    if aa[-1][0] <= pp[i][0] <= aa[-1][1] or aa[-1][0] <= pp[i][1] <= aa[-1][1] or pp[i][0] <= aa[-1][0] <= pp[i][1] or pp[i][0] <= aa[-1][1] <= pp[i][1]:
        aa[-1] = (min(aa[-1][0], pp[i][0]), max(aa[-1][1], pp[i][1]))
    else:
        aa.append(pp[i])

for a in aa:
    print(f'{(a[0] // 60):02d}{(a[0] % 60):02d}-{(a[1] // 60):02d}{(a[1] % 60):02d}')
