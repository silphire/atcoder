n, k = map(int, input().split())
s = [0] * n
for i in range(n):
    s[i] = int(input())
l = 0
x = 1
ans = 0
for r in range(n):
    if s[r] == 0:
        print(n)
        exit()
    x *= s[r]
    if x > k:
        x //= s[l]
        l += 1
    else:
        ans = max(ans, r - l + 1)
print(ans)