n, a, b, c = map(int, input().split())
ll = [int(input()) for _ in range(n)]

def dfs(x, aa, bb, cc):
    if x == n:
        if aa == 0 or bb == 0 or cc == 0:
            return float('inf')
        else:
            ans = abs(a - aa) + abs(b - bb) + abs(c - cc) - 30
            return ans
    return min([
        dfs(x + 1, aa, bb, cc),
        dfs(x + 1, aa + ll[x], bb, cc) + 10,
        dfs(x + 1, aa, bb + ll[x], cc) + 10,
        dfs(x + 1, aa, bb, cc + ll[x]) + 10,
    ])

print(dfs(0, 0, 0, 0))