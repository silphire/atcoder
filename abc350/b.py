n, q = map(int, input().split())
tt = list(map(int, input().split()))

f = [1] * n
for t in tt:
    f[t - 1] = 1 - f[t - 1]
print(sum(f))