a, b = map(int, input().split())
for x in range(a, b + 1):
    if x in {100, 50, 25, 20, 10, 5, 4, 2, 1}:
        print('Yes')
        exit()
print('No')