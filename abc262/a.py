y = int(input())
if y % 4 == 2:
    print(y)
elif y % 4 < 2:
    print(y + 2 - y % 4)
else:
    y += 4
    print(y + 2 - y % 4)
