n, w = map(int, input().split())
ma = [0] * 200002

maxt = 0
for i in range(n):
    s, t, p = map(int, input().split())
    ma[s] += p
    ma[t] -= p
    maxt = max(maxt, t)

if ma[0] > w:
    print('No')
    exit()
for i in range(1, maxt + 1):
    ma[i] += ma[i - 1]
    if ma[i] > w:
        print('No')
        exit()
print('Yes')