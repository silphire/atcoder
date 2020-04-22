a, b = map(int, input().split())
x = a + b
if x % 2 == 1:
    print("IMPOSSIBLE")
else:
    print(x // 2)
