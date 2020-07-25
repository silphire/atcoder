n = int(input())
aa = list(map(int, input().split()))

if n == 1:
    print(0)
    exit(0)

for i in range(n):
    aa[i] -= i + 1

aa = sorted(aa)
b1 = aa[n//2]
b2 = aa[n//2 + 1]
ans = min(
    sum([abs(a - b1) for a in aa]),
    sum([abs(a - b2) for a in aa])
)
print(ans)
