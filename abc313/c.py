n = int(input())
aa = list(sorted(map(int, input().split())))

ans = 0
s = sum(aa)
x = s // n
r = s % n
for i, a in enumerate(aa):
    p = int(i >= n - r)
    ans += abs(x + p - a)
print(ans // 2)
