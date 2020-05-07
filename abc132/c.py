n = int(input())
d = list(map(int, input().split()))

d = sorted(d)
x = d[n // 2] - d[n // 2 - 1]
print(max(0, x))