a, b = map(int, input().split())
for c in range(1, 4):
    if a * b * c % 2 == 1:
        print('Yes')
        exit(0)
print('No')