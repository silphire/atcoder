n, m = map(int, input().split())
ss = list(map(int, input().split()))
tt = list(map(int, input().split()))
if set(ss) != set(tt):
    print(-1)
    exit()
if len(set(ss)) == 0:
    print(0)
    exit()

d = 0
for i in range(1, n):
    if ss[0] != ss[i] or ss[0] != ss[-i]:
        d = i
        break
c = 0
for i in range(1, n):
    if ss[i - 1] != ss[i]:
        c += 1
x = len(tt) + c + d
if ss[0] != tt[0]:
    x += 1
print(x)
