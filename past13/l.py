def lis(xs):
    """ return: LISの長さ
    """
    n = len(xs)
    if n == 0:
        return 0

    import bisect
    dp = []
    for i in range(n):
        p = bisect.bisect_right(dp, xs[i])
        if p == len(dp):
            dp.append(xs[i])
        else:
            dp[p] = xs[i]
    return len(dp)


n = int(input())
lr = sorted([
    tuple(map(int, input().split()))
    for _ in range(n)
], key=lambda x: (-x[1], x[0]))
print(lis([x[0] for x in lr]))
