def lcs(s: str, t: str) -> int:
    """最長部分共通列 (longest common sequence)
    """
    ns = len(s)
    nt = len(t)
    dp = [[0] * (nt + 1) for _ in range(ns + 1)]
    for i in range(ns):
        for j in range(nt):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], dp[i][j] + 1)
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i + 1][j], dp[i][j + 1])
    return dp[ns][nt]

print(lcs(input(), input()))