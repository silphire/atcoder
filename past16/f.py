MOD = 998244353
ss = list(input().split('*'))
a = 1
for s in ss:
    x = 0
    for c in s:
        x = (x * 10 + int(c)) % MOD
    a = a * x % MOD
print(a)