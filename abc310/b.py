n, m = map(int, input().split())
pp = [0] * n
cc = [0] * n
ff = [None] * n
for i in range(n):
    pp[i], cc[i], *ff[i] = map(int, input().split())
    ff[i] = set(ff[i])

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if pp[i] < pp[j]:
            continue
        if not ff[i].issubset(ff[j]):
            continue
        if pp[i] > pp[j] or len(ff[j] - ff[i]) > 0:
            print('Yes')
            exit()
print('No')