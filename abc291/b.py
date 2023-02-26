n = int(input())
xx = list(sorted(map(int, input().split())))
print(sum(xx[n:-n]) / (3 * n))