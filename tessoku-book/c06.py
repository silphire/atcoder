n = int(input())
print(n)
for i in range(n):
    print(f'{i % n + 1} {(i + 1) % n + 1}')