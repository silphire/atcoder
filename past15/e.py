import itertools

n, k = map(int, input().split())
aa = list(map(int, input().split()))

ans = 0
for ii in itertools.combinations(range(n), k):
    ans += sum(aa[i] for i in ii)
print(ans)