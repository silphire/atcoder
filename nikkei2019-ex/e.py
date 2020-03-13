nn = int(input())
for n in range(1, nn + 1):
    s = ''
    for x in range(5):
        if n % (x + 2) == 0:
            s += list('abcde')[x]
    if len(s) > 0:
        print(s)
    else:
        print(n)
