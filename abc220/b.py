k = int(input())
a, b = input().rstrip().split()
aa = 0
for c in list(a):
    aa = aa * k + int(c)
bb = 0
for c in list(b):
    bb = bb * k + int(c)
print(aa * bb)