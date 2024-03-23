n, k = map(int, input().split())
a = sum(set([x for x in map(int, input().split()) if x <= k]))
ans = k * (k + 1) // 2 - a
print(ans)