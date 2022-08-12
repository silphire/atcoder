a, b = map(int, input().split())

if a == 0 or b == 0 or (a < 0 and b > 0):
    print("Zero")
    exit()
elif a > 0:
    print("Positive")
else:
    if (b - a) % 2 == 1:
        print('Positive')
    else:
        print('Negative')