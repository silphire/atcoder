s = input().rstrip()
x = s.find('o')
if x < 0:
    print("none")
else:
    print(x // 4 + 1)