n = int(input())

ff = {}
f = 5
i = 1
while f < 10 ** 18:
    ff[f] = i
    f *= 5
    i += 1

t = 3
i = 1
while n - t >= 0:
    if (n - t) in ff:
        print(f"{i} {ff[n - t]}")
        exit()
    i += 1
    t *= 3


print("-1")
