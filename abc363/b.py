n, t, p = map(int, input().split())
ll = sorted(map(int, input().split()), reverse=True)
print(max(0, t - ll[p - 1]))
