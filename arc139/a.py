n = int(input())
tt = list(map(int, input().split()))

a = 0
for t in tt:
    a = (a >> t) + 1
    if a & 1 == 0:
        a += 1
    a <<= t
print(a)