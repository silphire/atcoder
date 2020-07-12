n, k = map(int, input().split())
xx = tuple(map(int, input().split()))

ans = 10 ** 9
for i in range(n - k + 1):
    if xx[i + k - 1] <= 0:
        ans = min(ans, -xx[i])
    elif xx[i] >= 0:
        ans = min(ans, xx[i + k - 1])
    else: #if xx[i] <= 0 and xx[i + k - 1] >= 0:
        ans = min(
            ans,
            -xx[i] * 2 + xx[i + k - 1],
            -xx[i] + 2 * xx[i + k - 1]
        )
print(ans)
