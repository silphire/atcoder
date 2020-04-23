n = int(input())
p = list(map(int, input().split()))
q = sorted(p)
x = 0
for i in range(len(p)):
    if p[i] != q[i]:
        x += 1
if x == 2 or x == 0:
    print("YES")
else:
    print("NO")