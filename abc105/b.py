n = int(input())
for x in range(100):
    for y in range(100):
        if n == x * 4 + y * 7:
            print('Yes')
            exit(0)
print('No')