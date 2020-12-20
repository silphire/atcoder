n, t = map(int, input().split())
tt = list(map(int, input().split()))

ans = 0
stop = 0
for tc in tt:
    if tc < stop:
        ans += t + tc - stop
    else:
        ans += t
    stop = tc + t
print(ans)