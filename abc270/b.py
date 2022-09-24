x, y, z = map(int, input().split())
if 0 < x < y:
    print(x)
elif 0 < y < x:
    if y < z:
        print(-1)
    else:
        if z < 0:
            print(x - z * 2)
        else:
            print(x)
elif y < x < 0:
    print(-x)
elif x < y < 0:
    if z < y:
        print(-1)
    else:
        if z > 0:
            print(z * 2 - x)
        else:
            print(-x)
else:
    print(abs(x))