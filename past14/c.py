n = int(input())
pp = list(map(int, input().split()))
xx = [None] * n
for i, p in enumerate(pp):
    xx[p - 1] = i + 1
print(*xx)