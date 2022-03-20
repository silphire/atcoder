ss = input().rstrip().split()
tt = input().rstrip().split()

d = {ss[i]: i for i in range(3)}
uu = [d[t] for t in tt]

c = 0
for i in range(3):
    if i == uu[i]:
        c += 1

if c == 1:
    print("No")
else:
    print("Yes")