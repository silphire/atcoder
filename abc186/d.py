n = int(input())
aa = list(sorted(map(int, input().split())))

ans = 0
x = sum(aa)
for i in range(n):
    last = aa[-i - 1]
    x -= last
    ans += last * (n - 1 - i) - x
print(ans)
