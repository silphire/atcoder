k, n = map(int, input().split())
aa = list(map(int, input().split()))
 
mdiff = 0
for i in range(n):
    mdiff = max(mdiff, abs(k + aa[i] - aa[i - 1]) % k)
if n == 2:
    print(mdiff)
else:
    print(k - mdiff)
