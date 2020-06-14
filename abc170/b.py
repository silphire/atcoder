x, y = map(int, input().split())

for i in range(x + 1):
    z = i * 2 + 4 * (x - i)
    if z == y:
        print("Yes")
        exit(0)
print("No")