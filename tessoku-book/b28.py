MOD = 1000000007
n = int(input())
aa = [0] * (n + 1)
aa[1] = aa[2] = 1
for i in range(3, n + 1):
    aa[i] = aa[i - 1] + aa[i - 2]
    aa[i] %= MOD
print(aa[n])