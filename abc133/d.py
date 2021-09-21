n = int(input())
aa = list(map(int, input().split()))
ans = [0] * n
x1 = 0
for i in range(n):
    if i % 2 == 0:
        ans[0] += aa[i]
    else:
        ans[0] -= aa[i]
for i in range(1, n):
    ans[i] = 2 * aa[i - 1] - ans[i - 1]
print(' '.join(map(str, ans)))