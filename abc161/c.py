n, k = map(int, input().split())

n = n % k
ans = n
while True:
    ans = min(ans, n)
    n = abs(n - k)
    if n <= ans:
        break
print(n)