n = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input()) - 1

x = 0
p = set()
while x != 1:
    p.add(x)
    x = a[x]
    if x in p:
        print("-1")
        exit()
print(len(p))