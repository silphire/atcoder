n, m = map(int, input().split())

def dfs(a):
    global n, m
    if len(a) == n:
        return [a]
    ans = []
    for x in range(1 + (a[-1] if a else 0), m + 1):
        ans.extend(dfs(a + (x,)))
    return ans

for a in sorted(dfs(())):
    print(*a)