a, b, c = map(int, input().split())
f1 = a + b == c
f2 = a - b == c
print(["!", "-", "+", "?"][int(f1) * 2 + int(f2)])