x, y = map(int, input().split())

a = max(0, 4 - x) + max(0, 4 - y) + int(x == 1 and y == 1) * 4
print(a * 100000)