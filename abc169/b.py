n = int(input())
a = tuple(sorted(map(int, input().split())))
x = 1
for aa in a:
    x *= aa
    if x > 10 ** 18:
        print(-1)
        exit(0)
print(x)
