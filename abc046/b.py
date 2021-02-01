n, k = map(int, input().split())
x = k
for i in range(1, n):
    x *= k - 1
print(x)