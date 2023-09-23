n, x = map(int, input().split())
aa = list(sorted(map(int, input().split())))

mi = aa[0]
ma = aa[-1]
s = sum(aa)
for a in range(101):
    if a <= mi:
        if x <= s - ma:
            print(a)
            exit()
    elif a >= ma:
        if x <= s - mi:
            print(a)
            exit()
    elif x <= s + a - ma - mi:
        print(a)
        exit()
print(-1)