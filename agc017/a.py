n, p = map(int, input().split())
aa = list(map(int, input().split()))

if sum([a % 2 for a in aa]) == 0:
    print((1 - p) * 2 ** n)
else:
    print(2 ** (n - 1))