n = int(input())
work = [None] * n
for i in range(n):
    work[i] = tuple(map(int, input().split()))
work = sorted(work, key=lambda x: x[1])
t = 0
f = True
for i, w in enumerate(work):
    t += w[0]
    if t > w[1]:
        f = False
        break
if f:
    print("Yes")
else:
    print("No")