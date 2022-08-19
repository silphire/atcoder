n = int(input())
aa = list(map(int, input().split()))
x = 1
for a in aa:
    if a % 2 == 0:
        x *= 2
print(3 ** n - x)