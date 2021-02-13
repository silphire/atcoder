n = int(input())

tt, aa = 1, 1
for i in range(n):
    t, a = map(int, input().split())
    x = max((tt - 1) // t, (aa - 1) // a) + 1
    tt = x * t
    aa = x * a

print(tt + aa)