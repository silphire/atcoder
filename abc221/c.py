import itertools

n = list(input().rstrip())
nn = len(n)
ans = 0
for p in itertools.permutations(n):
    for i in range(nn):
        x = p[:i]
        y = p[i:]
        if len(x) == 0 or len(y) == 0 or x[0] == '0' or y[0] == '0':
            continue
        ans = max(ans, int(''.join(x)) * int(''.join(y)))
print(ans)