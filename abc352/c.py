n = int(input())
aa = [None] * n
bb = [None] * n

for i in range(n):
    aa[i], bb[i] = map(int, input().split())

ans = 0
sa = sum(aa)
for i in range(n):
    ans = max(ans, sa - aa[i] + bb[i])
print(ans)