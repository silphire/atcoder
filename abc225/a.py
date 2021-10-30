s = input().rstrip()
n = len(set(list(s)))
if n == 3:
    print(6)
elif n == 2:
    print(3)
else:
    print(1)