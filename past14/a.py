n, s, t = map(int, input().split())
if n % 2 == 0:
    if s == 0:
        if t == 0:
            print('Bob')
        else:
            print('Alice')
    else:
        if t == 0:
            print('Alice')
        else:
            print('Bob')
else:
    if s == 0:
        if t == 0:
            print('Alice')
        else:
            print('Bob')
    else:
        if t == 0:
            print('Bob')
        else:
            print('Alice')
