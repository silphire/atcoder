n = int(input())
aa = list(map(int, input().split()))
for i in range(n - 1):
    s, t = map(int, input().split())
    aa[i + 1] += (aa[i] // s) * t
print(aa[-1])