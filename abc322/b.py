n, m = map(int, input().split())
s = input()
t = input()

f1 = f2 = False
if t[:n] == s:
    f1 = True
if t[m - n:] == s:
    f2 = True
if f1 and f2:
    print(0)
elif f1:
    print(1)
elif f2:
    print(2)
else:
    print(3)