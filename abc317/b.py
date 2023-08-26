n = int(input())
aa = list(sorted(map(int, input().split())))

s = (aa[0] + aa[0] + n) * (n + 1) // 2
print(s - sum(aa))