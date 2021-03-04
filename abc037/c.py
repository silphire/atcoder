n, k = map(int, input().split())
aa = list(map(int, input().split()))
ans = sum(aa) * k
for i in range(1, k):
    ans -= aa[k - 1 - i] * i
    ans -= aa[n - k + i] * i
print(ans)