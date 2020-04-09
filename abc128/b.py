n = int(input())
x = []
for i in range(n):
    s, p = input().rstrip().split()
    x.append((s, 100 - int(p), i + 1))
x = sorted(x)
for xx in x:
    print(xx[2])