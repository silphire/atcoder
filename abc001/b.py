m = int(input())
if m < 100:
    print('00')
elif m <= 5000:
    m //= 100
    print(f'{m:02d}')
elif m <= 30000:
    print(m // 1000 + 50)
elif m <= 70000:
    m //= 1000
    m -= 30
    m //= 5
    m += 80
    print(m)
else:
    print(89)