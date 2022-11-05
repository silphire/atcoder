s = input().rstrip()
x = s.rfind('a')
if x == -1:
    print(-1)
else:
    print(x + 1)