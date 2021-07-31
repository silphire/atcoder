x = list(map(int, list(input().rstrip())))
if len(set(x)) == 1:
    print('Weak')
    exit()
else:
    f = True
    for i in range(3):
        if (x[i] + 1) % 10 != x[i + 1]:
            f = False
            break
    if f:
        print('Weak')
    else:
        print('Strong')
