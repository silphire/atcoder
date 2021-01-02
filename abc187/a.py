a, b = input().rstrip().split()
a = sum(map(int, list(a)))
b = sum(map(int, list(b)))
print(max(a, b))