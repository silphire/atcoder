def edit_distance(s: str, t: str) -> int:
    """ 編集距離 (レーベンシュタイン距離)
    """
    ns = len(s)
    nt = len(t)

    if ns == 0:
        return nt
    elif nt == 0:
        return ns

    dp = [[0] * (nt + 1) for _ in range(ns + 1)]
    for i in range(ns + 1):
        dp[i][0] = i
    for j in range(nt + 1):
        dp[0][j] = j

    for i in range(1, ns + 1):
        for j in range(1, nt + 1):
            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + int(s[i - 1] != t[j - 1]),
            )

    return dp[ns][nt]

print(edit_distance(input(), input()))