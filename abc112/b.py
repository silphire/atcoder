n, t = map(int, input().split())
ans = 100000
for i in range(n):
    c, tt = map(int, input().split())
    if tt <= t:
        ans = min(ans, c)
if ans == 100000:
    print("TLE")
else:
    print(ans)
