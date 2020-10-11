dd = list(map(int, list(input())))
for i in range(2 ** 3):
    ans = dd[0]
    exp = str(dd[0])
    for j in range(3):
        if (i >> j) & 1 == 0:
            ans += dd[j + 1]
            exp += '+'
        else:
            ans -= dd[j + 1]
            exp += '-'
        exp += str(dd[j + 1])
    if ans == 7:
        print(exp + '=7')
        exit(0)
print("bad")