n, k = map(int, input().split())
a = tuple(map(int, input().split()))

ans = 0
i = 0
j = 0
x = 0
while i < n:
    while x < k:
        if j == n:
            print(ans)
            exit(0)
        x += a[j]
        j += 1
    ans += n - j + 1
    
    x -= a[i]
    i += 1
print(ans)
