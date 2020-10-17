s = input()
a, b = map(int, s.split())
if a >= 13:
    print(b)
elif 6 <= a <= 12:
    print(b // 2)
else:
    print(0)