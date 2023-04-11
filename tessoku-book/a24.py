def lis(xs):
    """ return: LISの長さ
    """
    n = len(xs)
    if n == 0:
        return 0

    import bisect
    dp = [xs[0]]
    for i in range(n):
        if xs[i] > dp[-1]:
            dp.append(xs[i])
        else:
            p = bisect.bisect_left(dp, xs[i])
            dp[p] = xs[i]
    return len(dp)

n = int(input())
print(lis(tuple(map(int, input().split()))))