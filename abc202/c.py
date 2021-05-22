from collections import Counter
n = int(input())
aa = tuple(map(int, input().split()))
bb = tuple(map(int, input().split()))
cc = tuple(map(int, input().split()))
dd = [bb[cc[i] - 1] for i in range(n)]
ca = Counter(aa)
cd = Counter(dd)
ans = 0
for x in set(ca) & set(cd):
    ans += ca[x] * cd[x]
print(ans)