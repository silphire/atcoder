import itertools
n = int(input())
aa = sorted(map(int, input().split()), reverse=True)
ans = 0
for xx in itertools.permutations(aa[:3], 3):
    ans = max(ans, int(''.join(map(str, xx))))
print(ans)