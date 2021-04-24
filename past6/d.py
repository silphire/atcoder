n, k = map(int, input().split())
a = list(map(int, input().split()))
b = [0] * (n + 1)
for i in range(n):
    b[i + 1] = b[i] + a[i]
for i in range(n - k + 1):
    print(b[i + k] - b[i])