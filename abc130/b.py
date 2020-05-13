n, x = map(int, input().split())
l = list(map(int, input().split()))

d = 0
for i in range(n):
    if d > x:
        print(i)
        exit(0)
    d += l[i]
if d > x:
    print(n)
else:
    print(n + 1)
